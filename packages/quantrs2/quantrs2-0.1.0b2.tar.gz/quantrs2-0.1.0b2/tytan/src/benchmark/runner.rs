//! Benchmark runner implementation

use crate::{
    benchmark::{
        analysis::PerformanceReport,
        hardware::{CpuBackend, HardwareBackend},
        metrics::{BenchmarkMetrics, QualityMetrics, TimingMetrics, UtilizationMetrics},
    },
    sampler::SASampler,
};
use scirs2_core::ndarray::Array2;
use scirs2_core::random::prelude::*;
use serde::{Deserialize, Serialize};
use std::{
    collections::HashMap,
    time::{Duration, Instant},
};

/// Benchmark configuration
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BenchmarkConfig {
    /// Problem sizes to test
    pub problem_sizes: Vec<usize>,
    /// Problem densities to test (fraction of non-zero elements)
    pub problem_densities: Vec<f64>,
    /// Number of samples per problem
    pub num_reads: usize,
    /// Number of repetitions for timing
    pub num_repetitions: usize,
    /// Backends to benchmark
    pub backends: Vec<String>,
    /// Sampler configurations
    pub sampler_configs: Vec<SamplerConfig>,
    /// Whether to save intermediate results
    pub save_intermediate: bool,
    /// Output directory for results
    pub output_dir: Option<String>,
    /// Maximum time per benchmark (seconds)
    pub timeout_seconds: u64,
}

/// Sampler configuration for benchmarking
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SamplerConfig {
    pub name: String,
    pub params: HashMap<String, f64>,
}

impl Default for BenchmarkConfig {
    fn default() -> Self {
        Self {
            problem_sizes: vec![10, 50, 100, 500, 1000],
            problem_densities: vec![0.1, 0.5, 1.0],
            num_reads: 100,
            num_repetitions: 3,
            backends: vec!["cpu".to_string()],
            sampler_configs: vec![
                SamplerConfig {
                    name: "SA".to_string(),
                    params: HashMap::from([
                        ("T_0".to_string(), 10.0),
                        ("T_f".to_string(), 0.01),
                        ("steps".to_string(), 1000.0),
                    ]),
                },
                SamplerConfig {
                    name: "GA".to_string(),
                    params: HashMap::from([
                        ("population_size".to_string(), 50.0),
                        ("max_generations".to_string(), 100.0),
                        ("mutation_rate".to_string(), 0.1),
                    ]),
                },
            ],
            save_intermediate: false,
            output_dir: None,
            timeout_seconds: 300,
        }
    }
}

/// Benchmark runner
pub struct BenchmarkRunner {
    config: BenchmarkConfig,
    backends: Vec<Box<dyn HardwareBackend>>,
    results: Vec<BenchmarkResult>,
}

/// Individual benchmark result
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BenchmarkResult {
    pub backend_name: String,
    pub sampler_name: String,
    pub problem_size: usize,
    pub problem_density: f64,
    pub metrics: BenchmarkMetrics,
    pub timestamp: std::time::SystemTime,
}

impl BenchmarkRunner {
    /// Create new benchmark runner
    pub fn new(config: BenchmarkConfig) -> Self {
        let backends = Self::create_backends(&config);

        Self {
            config,
            backends,
            results: Vec::new(),
        }
    }

    /// Create hardware backends based on configuration
    fn create_backends(config: &BenchmarkConfig) -> Vec<Box<dyn HardwareBackend>> {
        let mut backends: Vec<Box<dyn HardwareBackend>> = Vec::new();

        for backend_name in &config.backends {
            match backend_name.as_str() {
                "cpu" => {
                    // Create CPU backend with SA sampler as default
                    let sampler = Box::new(SASampler::new(None))
                        as Box<dyn crate::sampler::Sampler + Send + Sync>;
                    backends.push(Box::new(CpuBackend::new(sampler)));
                }
                #[cfg(feature = "gpu")]
                "gpu" => {
                    use crate::benchmark::hardware::GpuBackend;
                    backends.push(Box::new(GpuBackend::new(0)));
                }
                "quantum" => {
                    use crate::benchmark::hardware::QuantumBackend;
                    backends.push(Box::new(QuantumBackend::new("simulator".to_string())));
                }
                _ => {
                    eprintln!("Unknown backend: {}", backend_name);
                }
            }
        }

        backends
    }

    /// Run complete benchmark suite
    pub fn run_complete_suite(mut self) -> Result<PerformanceReport, Box<dyn std::error::Error>> {
        println!("Starting benchmark suite...");
        println!("Configuration: {:?}", self.config);

        // Initialize backends
        for backend in &mut self.backends {
            if !backend.is_available() {
                eprintln!("Backend {} is not available, skipping", backend.name());
                continue;
            }

            backend.initialize()?;
            println!("Initialized backend: {}", backend.name());
        }

        // Run benchmarks for each configuration
        let total_benchmarks = self.config.problem_sizes.len()
            * self.config.problem_densities.len()
            * self.config.sampler_configs.len()
            * self.backends.len();

        let mut completed = 0;

        for &problem_size in &self.config.problem_sizes {
            for &density in &self.config.problem_densities {
                // Generate test problem
                let matrix = self.generate_qubo_problem(problem_size, density);

                for sampler_config in &self.config.sampler_configs {
                    for backend_idx in 0..self.backends.len() {
                        if !self.backends[backend_idx].is_available() {
                            continue;
                        }

                        let backend_name = self.backends[backend_idx].name().to_string();
                        println!(
                            "Running benchmark {}/{}: {} - {} - size={}, density={}",
                            completed + 1,
                            total_benchmarks,
                            backend_name,
                            sampler_config.name,
                            problem_size,
                            density
                        );

                        let result = {
                            let backend = &mut self.backends[backend_idx];
                            Self::run_single_benchmark(
                                backend.as_mut(),
                                &sampler_config,
                                &matrix,
                                problem_size,
                                density,
                                self.config.num_reads,
                                self.config.num_repetitions,
                            )
                        };

                        match result {
                            Ok(result) => {
                                self.results.push(result);
                                completed += 1;
                            }
                            Err(e) => {
                                eprintln!("Benchmark failed: {}", e);
                            }
                        }

                        // Save intermediate results if requested
                        if self.config.save_intermediate {
                            self.save_intermediate_results()?;
                        }
                    }
                }
            }
        }

        // Generate performance report
        let report = PerformanceReport::from_results(&self.results)?;

        // Save final results
        if let Some(ref output_dir) = self.config.output_dir {
            self.save_results(&output_dir)?;
            report.save_to_file(&format!("{}/performance_report.json", output_dir))?;
        }

        Ok(report)
    }

    /// Run single benchmark
    fn run_single_benchmark(
        backend: &mut dyn HardwareBackend,
        sampler_config: &SamplerConfig,
        matrix: &Array2<f64>,
        problem_size: usize,
        density: f64,
        num_reads: usize,
        num_repetitions: usize,
    ) -> Result<BenchmarkResult, Box<dyn std::error::Error>> {
        let mut metrics = BenchmarkMetrics::new(problem_size, density);

        // Warm-up run
        let _ = backend.run_qubo(matrix, 1, sampler_config.params.clone())?;

        // Timing runs
        let mut timings = Vec::new();
        let mut all_results = Vec::new();

        for _ in 0..num_repetitions {
            // Measure memory before
            let mem_before = Self::get_memory_usage_static();

            let start = Instant::now();
            let _setup_start = start;

            // Run benchmark
            let results = backend.run_qubo(matrix, num_reads, sampler_config.params.clone())?;

            let total_time = start.elapsed();

            // Measure memory after
            let mem_after = Self::get_memory_usage_static();

            timings.push(total_time);
            all_results.extend(results);

            // Update memory metrics
            metrics.memory.peak_memory = metrics.memory.peak_memory.max(mem_after);
            metrics.memory.allocated = mem_after.saturating_sub(mem_before);
        }

        // Calculate timing statistics
        let avg_time = timings.iter().sum::<Duration>() / timings.len() as u32;
        metrics.timings = TimingMetrics {
            total_time: avg_time,
            setup_time: Duration::from_millis(10), // Estimate
            compute_time: avg_time - Duration::from_millis(10),
            postprocess_time: Duration::ZERO,
            time_per_sample: avg_time / num_reads as u32,
            time_to_solution: Some(timings[0]),
        };

        // Calculate quality metrics
        if !all_results.is_empty() {
            let energies: Vec<f64> = all_results.iter().map(|r| r.energy).collect();
            let best_energy = energies.iter().copied().fold(f64::INFINITY, f64::min);
            let avg_energy = energies.iter().sum::<f64>() / energies.len() as f64;
            let variance = energies
                .iter()
                .map(|e| (e - avg_energy).powi(2))
                .sum::<f64>()
                / (energies.len() - 1) as f64;

            metrics.quality = QualityMetrics {
                best_energy,
                avg_energy,
                energy_std: variance.sqrt(),
                success_probability: 0.0, // Would need known optimal
                time_to_target: None,
                unique_solutions: Self::count_unique_solutions(&all_results),
            };
        }

        // Get hardware metrics
        let hw_metrics = backend.get_metrics();
        metrics.utilization = UtilizationMetrics {
            cpu_usage: hw_metrics.get("cpu_threads").copied().unwrap_or(0.0),
            gpu_usage: hw_metrics.get("gpu_usage").copied(),
            memory_bandwidth: 0.0, // Placeholder
            cache_hit_rate: None,
            power_consumption: None,
        };

        Ok(BenchmarkResult {
            backend_name: backend.name().to_string(),
            sampler_name: sampler_config.name.clone(),
            problem_size,
            problem_density: density,
            metrics,
            timestamp: std::time::SystemTime::now(),
        })
    }

    /// Generate random QUBO problem
    fn generate_qubo_problem(&self, size: usize, density: f64) -> Array2<f64> {
        let mut rng = thread_rng();
        let mut matrix = Array2::zeros((size, size));

        // Generate symmetric matrix with given density
        for i in 0..size {
            for j in i..size {
                if rng.gen::<f64>() < density {
                    let value = rng.gen_range(-10.0..10.0);
                    matrix[[i, j]] = value;
                    if i != j {
                        matrix[[j, i]] = value;
                    }
                }
            }
        }

        matrix
    }

    /// Get current memory usage (static version)
    fn get_memory_usage_static() -> usize {
        // Simple implementation - in practice would use system-specific APIs
        #[cfg(feature = "scirs")]
        {
            if let Ok(usage) = crate::scirs_stub::scirs2_core::memory::get_current_usage() {
                return usage;
            }
        }

        // Fallback: estimate based on process info
        0
    }

    /// Count unique solutions
    fn count_unique_solutions(results: &[crate::sampler::SampleResult]) -> usize {
        use std::collections::HashSet;

        let unique: HashSet<Vec<bool>> = results
            .iter()
            .map(|r| {
                // Convert assignments to ordered vector
                let mut vars: Vec<_> = r.assignments.iter().collect();
                vars.sort_by_key(|(name, _)| name.as_str());
                vars.into_iter().map(|(_, &value)| value).collect()
            })
            .collect();

        unique.len()
    }

    /// Save intermediate results
    fn save_intermediate_results(&self) -> Result<(), Box<dyn std::error::Error>> {
        if let Some(ref dir) = self.config.output_dir {
            let path = format!("{}/intermediate_results.json", dir);
            let json = serde_json::to_string_pretty(&self.results)?;
            std::fs::write(path, json)?;
        }
        Ok(())
    }

    /// Save final results
    fn save_results(&self, output_dir: &str) -> Result<(), Box<dyn std::error::Error>> {
        std::fs::create_dir_all(output_dir)?;

        // Save raw results
        let results_path = format!("{}/benchmark_results.json", output_dir);
        let json = serde_json::to_string_pretty(&self.results)?;
        std::fs::write(results_path, json)?;

        // Save configuration
        let config_path = format!("{}/benchmark_config.json", output_dir);
        let config_json = serde_json::to_string_pretty(&self.config)?;
        std::fs::write(config_path, config_json)?;

        Ok(())
    }
}

/// Quick benchmark function for simple testing
pub fn quick_benchmark(
    problem_size: usize,
) -> Result<BenchmarkMetrics, Box<dyn std::error::Error>> {
    let config = BenchmarkConfig {
        problem_sizes: vec![problem_size],
        problem_densities: vec![0.5],
        num_reads: 10,
        num_repetitions: 1,
        ..Default::default()
    };

    let runner = BenchmarkRunner::new(config);
    let report = runner.run_complete_suite()?;

    Ok(report.summary.overall_metrics)
}
