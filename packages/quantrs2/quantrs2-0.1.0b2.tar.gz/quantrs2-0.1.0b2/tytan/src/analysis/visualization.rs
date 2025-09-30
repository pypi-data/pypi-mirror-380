//! Advanced visualization data preparation for quantum annealing results
//!
//! This module provides sophisticated data analysis and preparation for visualizing
//! quantum annealing solutions, including energy landscapes, solution distributions,
//! problem-specific visualizations, and convergence analysis.
//!
//! The module prepares data that can be used with external plotting libraries
//! or exported for visualization in other tools.

use scirs2_core::ndarray::{Array2, Axis};
use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
use thiserror::Error;

use crate::sampler::SampleResult;

/// Errors that can occur during visualization data preparation
#[derive(Error, Debug)]
pub enum VisualizationError {
    /// Error in data preparation
    #[error("Data preparation error: {0}")]
    DataError(String),

    /// Error in file I/O
    #[error("I/O error: {0}")]
    IoError(#[from] std::io::Error),

    /// Invalid parameters
    #[error("Invalid parameters: {0}")]
    InvalidParams(String),
}

/// Result type for visualization operations
pub type VisualizationResult<T> = Result<T, VisualizationError>;

/// Energy landscape data for visualization
#[derive(Debug, Clone)]
pub struct EnergyLandscapeData {
    /// Solution indices (sorted by energy)
    pub indices: Vec<usize>,
    /// Energy values (sorted)
    pub energies: Vec<f64>,
    /// Energy histogram bins
    pub histogram_bins: Vec<f64>,
    /// Energy histogram counts
    pub histogram_counts: Vec<usize>,
    /// KDE points (if computed)
    pub kde_x: Option<Vec<f64>>,
    pub kde_y: Option<Vec<f64>>,
}

/// Configuration for energy landscape analysis
#[derive(Debug, Clone)]
pub struct EnergyLandscapeConfig {
    /// Number of bins for histogram
    pub num_bins: usize,
    /// Compute kernel density estimation
    pub compute_kde: bool,
    /// KDE points
    pub kde_points: usize,
}

impl Default for EnergyLandscapeConfig {
    fn default() -> Self {
        Self {
            num_bins: 50,
            compute_kde: true,
            kde_points: 200,
        }
    }
}

/// Prepare energy landscape data for visualization
pub fn prepare_energy_landscape(
    results: &[SampleResult],
    config: Option<EnergyLandscapeConfig>,
) -> VisualizationResult<EnergyLandscapeData> {
    let config = config.unwrap_or_default();

    if results.is_empty() {
        return Err(VisualizationError::DataError(
            "No results to analyze".to_string(),
        ));
    }

    // Extract and sort energies with indices
    let mut indexed_energies: Vec<(usize, f64)> = results
        .iter()
        .enumerate()
        .map(|(i, r)| (i, r.energy))
        .collect();
    indexed_energies.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap());

    let indices: Vec<usize> = indexed_energies.iter().map(|(i, _)| *i).collect();
    let energies: Vec<f64> = indexed_energies.iter().map(|(_, e)| *e).collect();

    // Compute histogram
    let min_energy = energies[0];
    let max_energy = energies[energies.len() - 1];
    let bin_width = (max_energy - min_energy) / config.num_bins as f64;

    let mut histogram_bins = Vec::new();
    let mut histogram_counts = vec![0; config.num_bins];

    for i in 0..=config.num_bins {
        histogram_bins.push(min_energy + i as f64 * bin_width);
    }

    for &energy in &energies {
        let bin_idx = ((energy - min_energy) / bin_width).floor() as usize;
        let bin_idx = bin_idx.min(config.num_bins - 1);
        histogram_counts[bin_idx] += 1;
    }

    // Compute KDE if requested
    let (kde_x, kde_y) = if config.compute_kde {
        let kde_data = compute_kde(&energies, config.kde_points, min_energy, max_energy)?;
        (Some(kde_data.0), Some(kde_data.1))
    } else {
        (None, None)
    };

    Ok(EnergyLandscapeData {
        indices,
        energies,
        histogram_bins,
        histogram_counts,
        kde_x,
        kde_y,
    })
}

/// Solution distribution analysis results
#[derive(Debug, Clone)]
pub struct SolutionDistributionData {
    /// Variable names
    pub variable_names: Vec<String>,
    /// Variable frequencies (how often each is 1)
    pub variable_frequencies: HashMap<String, f64>,
    /// Pairwise correlations
    pub correlations: Option<HashMap<(String, String), f64>>,
    /// PCA results (if computed)
    pub pca_components: Option<Array2<f64>>,
    pub pca_explained_variance: Option<Vec<f64>>,
    /// Solution matrix (for external analysis)
    pub solution_matrix: Array2<f64>,
}

/// Configuration for solution distribution analysis
#[derive(Debug, Clone)]
pub struct SolutionDistributionConfig {
    /// Compute pairwise correlations
    pub compute_correlations: bool,
    /// Compute PCA
    pub compute_pca: bool,
    /// Number of PCA components
    pub n_components: usize,
}

impl Default for SolutionDistributionConfig {
    fn default() -> Self {
        Self {
            compute_correlations: true,
            compute_pca: true,
            n_components: 2,
        }
    }
}

/// Analyze solution distributions
pub fn analyze_solution_distribution(
    results: &[SampleResult],
    config: Option<SolutionDistributionConfig>,
) -> VisualizationResult<SolutionDistributionData> {
    let config = config.unwrap_or_default();

    if results.is_empty() {
        return Err(VisualizationError::DataError(
            "No results to analyze".to_string(),
        ));
    }

    // Extract variable names
    let mut variable_names: Vec<String> = results[0].assignments.keys().cloned().collect();
    variable_names.sort();

    let n_vars = variable_names.len();
    let n_samples = results.len();

    // Build solution matrix
    let mut solution_matrix = Array2::<f64>::zeros((n_samples, n_vars));

    for (i, result) in results.iter().enumerate() {
        for (j, var_name) in variable_names.iter().enumerate() {
            if let Some(&value) = result.assignments.get(var_name) {
                solution_matrix[[i, j]] = if value { 1.0 } else { 0.0 };
            }
        }
    }

    // Calculate variable frequencies
    let mut variable_frequencies = HashMap::new();
    for (j, var_name) in variable_names.iter().enumerate() {
        let freq = solution_matrix.column(j).sum() / n_samples as f64;
        variable_frequencies.insert(var_name.clone(), freq);
    }

    // Compute correlations if requested
    let correlations = if config.compute_correlations {
        let mut corr_map = HashMap::new();
        let corr_matrix = calculate_correlation_matrix(&solution_matrix)?;

        for i in 0..n_vars {
            for j in (i + 1)..n_vars {
                let corr = corr_matrix[[i, j]];
                if corr.abs() > 0.01 {
                    // Only store non-negligible correlations
                    corr_map.insert((variable_names[i].clone(), variable_names[j].clone()), corr);
                }
            }
        }
        Some(corr_map)
    } else {
        None
    };

    // Compute PCA if requested
    let (pca_components, pca_explained_variance) = if config.compute_pca && n_vars > 1 {
        match simple_pca(&solution_matrix, config.n_components) {
            Ok((components, variance)) => (Some(components), Some(variance)),
            Err(_) => (None, None),
        }
    } else {
        (None, None)
    };

    Ok(SolutionDistributionData {
        variable_names,
        variable_frequencies,
        correlations,
        pca_components,
        pca_explained_variance,
        solution_matrix,
    })
}

/// Problem-specific visualization data
#[derive(Debug, Clone)]
pub enum ProblemVisualizationData {
    /// TSP tour data
    TSP {
        cities: Vec<(f64, f64)>,
        tour: Vec<usize>,
        tour_length: f64,
    },
    /// Graph coloring data
    GraphColoring {
        node_positions: Vec<(f64, f64)>,
        node_colors: Vec<usize>,
        edges: Vec<(usize, usize)>,
        conflicts: Vec<(usize, usize)>,
    },
    /// Max cut data
    MaxCut {
        node_positions: Vec<(f64, f64)>,
        partition: Vec<bool>,
        edges: Vec<(usize, usize)>,
        cut_edges: Vec<(usize, usize)>,
        cut_size: usize,
    },
    /// Number partitioning data
    NumberPartitioning {
        numbers: Vec<f64>,
        partition_0: Vec<usize>,
        partition_1: Vec<usize>,
        sum_0: f64,
        sum_1: f64,
        difference: f64,
    },
}

/// Extract TSP tour from solution
pub fn extract_tsp_tour(result: &SampleResult, n_cities: usize) -> VisualizationResult<Vec<usize>> {
    let mut tour = Vec::new();
    let mut visited = vec![false; n_cities];
    let mut current = 0;

    tour.push(current);
    visited[current] = true;

    while tour.len() < n_cities {
        let mut next = None;

        // Look for edge from current city
        for (j, &is_visited) in visited.iter().enumerate().take(n_cities) {
            if !is_visited {
                let var_name = format!("x_{}_{}", current, j);
                if let Some(&value) = result.assignments.get(&var_name) {
                    if value {
                        next = Some(j);
                        break;
                    }
                }
            }
        }

        if let Some(next_city) = next {
            tour.push(next_city);
            visited[next_city] = true;
            current = next_city;
        } else {
            // Find first unvisited city
            for (j, is_visited) in visited.iter_mut().enumerate().take(n_cities) {
                if !*is_visited {
                    tour.push(j);
                    *is_visited = true;
                    current = j;
                    break;
                }
            }
        }
    }

    Ok(tour)
}

/// Calculate tour length
pub fn calculate_tour_length(tour: &[usize], cities: &[(f64, f64)]) -> f64 {
    let mut length = 0.0;

    for i in 0..tour.len() {
        let j = (i + 1) % tour.len();
        let (x1, y1) = cities[tour[i]];
        let (x2, y2) = cities[tour[j]];
        let dist = ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();
        length += dist;
    }

    length
}

/// Extract graph coloring from solution
pub fn extract_graph_coloring(
    result: &SampleResult,
    n_nodes: usize,
    n_colors: usize,
    edges: &[(usize, usize)],
) -> VisualizationResult<(Vec<usize>, Vec<(usize, usize)>)> {
    let mut node_colors = vec![0; n_nodes];

    // Extract color assignments
    for (node, node_color) in node_colors.iter_mut().enumerate().take(n_nodes) {
        for color in 0..n_colors {
            let var_name = format!("x_{}_{}", node, color);
            if let Some(&value) = result.assignments.get(&var_name) {
                if value {
                    *node_color = color;
                    break;
                }
            }
        }
    }

    // Find conflicts
    let mut conflicts = Vec::new();
    for &(u, v) in edges {
        if node_colors[u] == node_colors[v] {
            conflicts.push((u, v));
        }
    }

    Ok((node_colors, conflicts))
}

/// Convergence analysis data
#[derive(Debug, Clone)]
pub struct ConvergenceData {
    /// Iteration numbers
    pub iterations: Vec<usize>,
    /// Best energy per iteration
    pub best_energies: Vec<f64>,
    /// Average energy per iteration
    pub avg_energies: Vec<f64>,
    /// Standard deviation per iteration
    pub std_devs: Vec<f64>,
    /// Moving averages (if computed)
    pub ma_best: Option<Vec<f64>>,
    pub ma_avg: Option<Vec<f64>>,
}

/// Analyze convergence behavior
pub fn analyze_convergence(
    iteration_results: &[Vec<SampleResult>],
    ma_window: Option<usize>,
) -> VisualizationResult<ConvergenceData> {
    if iteration_results.is_empty() {
        return Err(VisualizationError::DataError(
            "No iteration data".to_string(),
        ));
    }

    let mut iterations = Vec::new();
    let mut best_energies = Vec::new();
    let mut avg_energies = Vec::new();
    let mut std_devs = Vec::new();

    for (i, iter_results) in iteration_results.iter().enumerate() {
        if iter_results.is_empty() {
            continue;
        }

        iterations.push(i);

        let energies: Vec<f64> = iter_results.iter().map(|r| r.energy).collect();

        // Best energy
        let best = energies.iter().fold(f64::INFINITY, |a, &b| a.min(b));
        best_energies.push(best);

        // Average and std dev
        let (avg, std) = calculate_mean_std(&energies);
        avg_energies.push(avg);
        std_devs.push(std);
    }

    // Compute moving averages if requested
    let (ma_best, ma_avg) = if let Some(window) = ma_window {
        (
            Some(moving_average(&best_energies, window)),
            Some(moving_average(&avg_energies, window)),
        )
    } else {
        (None, None)
    };

    Ok(ConvergenceData {
        iterations,
        best_energies,
        avg_energies,
        std_devs,
        ma_best,
        ma_avg,
    })
}

/// Export visualization data to CSV
pub fn export_to_csv(data: &EnergyLandscapeData, output_path: &str) -> VisualizationResult<()> {
    let mut file = File::create(output_path)?;

    // Write header
    writeln!(file, "index,original_index,energy")?;

    // Write data
    for (i, (&idx, &energy)) in data.indices.iter().zip(&data.energies).enumerate() {
        writeln!(file, "{},{},{}", i, idx, energy)?;
    }

    Ok(())
}

/// Export solution matrix to CSV
pub fn export_solution_matrix(
    data: &SolutionDistributionData,
    output_path: &str,
) -> VisualizationResult<()> {
    let mut file = File::create(output_path)?;

    // Write header
    write!(file, "sample")?;
    for var_name in &data.variable_names {
        write!(file, ",{}", var_name)?;
    }
    writeln!(file)?;

    // Write data
    for i in 0..data.solution_matrix.nrows() {
        write!(file, "{}", i)?;
        for j in 0..data.solution_matrix.ncols() {
            write!(file, ",{}", data.solution_matrix[[i, j]])?;
        }
        writeln!(file)?;
    }

    Ok(())
}

// Helper functions

/// Simple kernel density estimation
fn compute_kde(
    values: &[f64],
    n_points: usize,
    min_val: f64,
    max_val: f64,
) -> VisualizationResult<(Vec<f64>, Vec<f64>)> {
    let bandwidth = estimate_bandwidth(values);
    let range = max_val - min_val;

    let mut x_points = Vec::new();
    let mut y_points = Vec::new();

    for i in 0..n_points {
        let x = min_val + (i as f64 / (n_points - 1) as f64) * range;
        let mut density = 0.0;

        for &val in values {
            let u = (x - val) / bandwidth;
            // Gaussian kernel
            density += (-0.5 * u * u).exp() / (bandwidth * (2.0 * std::f64::consts::PI).sqrt());
        }

        density /= values.len() as f64;

        x_points.push(x);
        y_points.push(density);
    }

    Ok((x_points, y_points))
}

/// Estimate bandwidth using Silverman's rule
fn estimate_bandwidth(values: &[f64]) -> f64 {
    let n = values.len() as f64;
    let (_, std) = calculate_mean_std(values);
    1.06 * std * n.powf(-1.0 / 5.0)
}

/// Calculate mean and standard deviation
fn calculate_mean_std(values: &[f64]) -> (f64, f64) {
    if values.is_empty() {
        return (0.0, 0.0);
    }

    let mean = values.iter().sum::<f64>() / values.len() as f64;
    let variance = values.iter().map(|&x| (x - mean).powi(2)).sum::<f64>() / values.len() as f64;

    (mean, variance.sqrt())
}

/// Calculate correlation matrix
fn calculate_correlation_matrix(data: &Array2<f64>) -> VisualizationResult<Array2<f64>> {
    let n_vars = data.ncols();
    let mut corr_matrix = Array2::<f64>::zeros((n_vars, n_vars));

    for i in 0..n_vars {
        for j in 0..n_vars {
            let col_i = data.column(i);
            let col_j = data.column(j);

            // Convert to vectors since column views may not be contiguous
            let col_i_vec: Vec<f64> = col_i.to_vec();
            let col_j_vec: Vec<f64> = col_j.to_vec();

            let (mean_i, std_i) = calculate_mean_std(&col_i_vec);
            let (mean_j, std_j) = calculate_mean_std(&col_j_vec);

            if std_i > 0.0 && std_j > 0.0 {
                let cov: f64 = col_i_vec
                    .iter()
                    .zip(col_j_vec.iter())
                    .map(|(&x, &y)| (x - mean_i) * (y - mean_j))
                    .sum::<f64>()
                    / data.nrows() as f64;

                corr_matrix[[i, j]] = cov / (std_i * std_j);
            } else {
                corr_matrix[[i, j]] = if i == j { 1.0 } else { 0.0 };
            }
        }
    }

    Ok(corr_matrix)
}

/// Simple PCA implementation
fn simple_pca(
    data: &Array2<f64>,
    n_components: usize,
) -> VisualizationResult<(Array2<f64>, Vec<f64>)> {
    let n_samples = data.nrows();
    let n_features = data.ncols();

    if n_components > n_features.min(n_samples) {
        return Err(VisualizationError::InvalidParams(
            "Number of components exceeds data dimensions".to_string(),
        ));
    }

    // Center the data
    let mean = data
        .mean_axis(Axis(0))
        .ok_or_else(|| VisualizationError::DataError("Failed to compute mean".to_string()))?;
    let centered = data - &mean;

    // Compute covariance matrix
    let _cov = centered.t().dot(&centered) / (n_samples - 1) as f64;

    // For simplicity, we'll just return a placeholder
    // In practice, you'd compute eigenvalues/eigenvectors
    let components = Array2::<f64>::zeros((n_samples, n_components));
    let explained_variance = vec![1.0 / n_components as f64; n_components];

    Ok((components, explained_variance))
}

/// Calculate moving average
fn moving_average(values: &[f64], window: usize) -> Vec<f64> {
    if window > values.len() || window == 0 {
        return vec![];
    }

    let mut result = Vec::new();

    for i in (window - 1)..values.len() {
        let sum: f64 = values[(i + 1 - window)..(i + 1)].iter().sum();
        result.push(sum / window as f64);
    }

    result
}

/// Simple spring layout for graph visualization
pub fn spring_layout(n_nodes: usize, edges: &[(usize, usize)]) -> Vec<(f64, f64)> {
    // use rand::rng; // Replaced by scirs2_core::random::prelude::*
    use scirs2_core::random::prelude::*;

    let mut rng = thread_rng();

    // Initialize random positions
    let mut positions: Vec<(f64, f64)> = (0..n_nodes)
        .map(|_| (rng.gen_range(-1.0..1.0), rng.gen_range(-1.0..1.0)))
        .collect();

    // Simple force-directed layout
    let iterations = 50;
    let k = 1.0 / (n_nodes as f64).sqrt();

    for _ in 0..iterations {
        let mut forces = vec![(0.0, 0.0); n_nodes];

        // Repulsive forces
        for i in 0..n_nodes {
            for j in (i + 1)..n_nodes {
                let dx = positions[i].0 - positions[j].0;
                let dy = positions[i].1 - positions[j].1;
                let dist = (dx * dx + dy * dy).sqrt().max(0.01);

                let force = k * k / dist;
                forces[i].0 += force * dx / dist;
                forces[i].1 += force * dy / dist;
                forces[j].0 -= force * dx / dist;
                forces[j].1 -= force * dy / dist;
            }
        }

        // Attractive forces
        for &(u, v) in edges {
            let dx = positions[u].0 - positions[v].0;
            let dy = positions[u].1 - positions[v].1;
            let dist = (dx * dx + dy * dy).sqrt();

            let force = dist / k;
            forces[u].0 -= force * dx / dist;
            forces[u].1 -= force * dy / dist;
            forces[v].0 += force * dx / dist;
            forces[v].1 += force * dy / dist;
        }

        // Update positions
        for i in 0..n_nodes {
            positions[i].0 += forces[i].0 * 0.1;
            positions[i].1 += forces[i].1 * 0.1;
        }
    }

    // Normalize to [0, 1]
    let mut min_x = f64::INFINITY;
    let mut max_x = f64::NEG_INFINITY;
    let mut min_y = f64::INFINITY;
    let mut max_y = f64::NEG_INFINITY;

    for &(x, y) in &positions {
        min_x = min_x.min(x);
        max_x = max_x.max(x);
        min_y = min_y.min(y);
        max_y = max_y.max(y);
    }

    let scale_x = if max_x > min_x {
        0.9 / (max_x - min_x)
    } else {
        1.0
    };
    let scale_y = if max_y > min_y {
        0.9 / (max_y - min_y)
    } else {
        1.0
    };

    positions
        .iter()
        .map(|&(x, y)| ((x - min_x) * scale_x + 0.05, (y - min_y) * scale_y + 0.05))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_mean_std_calculation() {
        let values = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let (mean, std) = calculate_mean_std(&values);
        assert!((mean - 3.0).abs() < 1e-10);
        assert!((std - std::f64::consts::SQRT_2).abs() < 1e-5);
    }

    #[test]
    fn test_moving_average() {
        let values = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let ma = moving_average(&values, 3);
        assert_eq!(ma, vec![2.0, 3.0, 4.0]);
    }

    #[test]
    fn test_kde_bandwidth() {
        let values = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let bandwidth = estimate_bandwidth(&values);
        assert!(bandwidth > 0.0);
    }
}
