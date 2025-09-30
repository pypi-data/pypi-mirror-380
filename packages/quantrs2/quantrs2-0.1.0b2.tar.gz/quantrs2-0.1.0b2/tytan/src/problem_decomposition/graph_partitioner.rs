//! Graph partitioning algorithms for QUBO problems

use super::types::*;
use scirs2_core::ndarray::{Array1, Array2};
use scirs2_core::random::prelude::*;
use scirs2_core::SliceRandomExt;
use std::collections::HashMap;

/// Automatic graph partitioner for QUBO problems
pub struct GraphPartitioner {
    /// Partitioning algorithm
    algorithm: PartitioningAlgorithm,
    /// Number of partitions
    num_partitions: usize,
    /// Balance constraint
    balance_factor: f64,
    /// Edge cut minimization weight
    edge_cut_weight: f64,
    /// Use multilevel partitioning
    use_multilevel: bool,
    /// Maximum recursion depth for multilevel algorithms
    max_recursion_depth: usize,
}

impl Default for GraphPartitioner {
    fn default() -> Self {
        Self::new()
    }
}

impl GraphPartitioner {
    /// Create new graph partitioner with default settings
    pub fn new() -> Self {
        Self {
            algorithm: PartitioningAlgorithm::Spectral,
            num_partitions: 2,
            balance_factor: 0.1,
            edge_cut_weight: 1.0,
            use_multilevel: true,
            max_recursion_depth: 10,
        }
    }

    /// Create new graph partitioner with specific settings
    pub fn with_config(algorithm: PartitioningAlgorithm, num_partitions: usize) -> Self {
        Self {
            algorithm,
            num_partitions,
            balance_factor: 0.1,
            edge_cut_weight: 1.0,
            use_multilevel: true,
            max_recursion_depth: 10,
        }
    }

    /// Set number of partitions
    pub fn with_num_partitions(mut self, num_partitions: usize) -> Self {
        self.num_partitions = num_partitions;
        self
    }

    /// Set partitioning algorithm
    pub fn with_algorithm(mut self, algorithm: PartitioningAlgorithm) -> Self {
        self.algorithm = algorithm;
        self
    }

    /// Set balance factor
    pub fn with_balance_factor(mut self, factor: f64) -> Self {
        self.balance_factor = factor;
        self
    }

    /// Set edge cut weight
    pub fn with_edge_cut_weight(mut self, weight: f64) -> Self {
        self.edge_cut_weight = weight;
        self
    }

    /// Simple partition method that returns subproblems
    pub fn partition(&self, qubo: &Array2<f64>) -> Result<Vec<Subproblem>, String> {
        // Create a simple variable map
        let n = qubo.shape()[0];
        let mut var_map = HashMap::new();
        for i in 0..n {
            var_map.insert(format!("x{}", i), i);
        }

        let partitioning = self.partition_qubo(qubo, &var_map)?;
        Ok(partitioning.subproblems)
    }

    /// Partition QUBO problem
    pub fn partition_qubo(
        &self,
        qubo: &Array2<f64>,
        var_map: &HashMap<String, usize>,
    ) -> Result<Partitioning, String> {
        // Build graph from QUBO
        let graph = self.build_graph_from_qubo(qubo)?;

        // Apply partitioning algorithm
        let partition_assignment = match self.algorithm {
            PartitioningAlgorithm::KernighanLin => self.kernighan_lin_partition(&graph)?,
            PartitioningAlgorithm::Spectral => self.spectral_partition(&graph)?,
            PartitioningAlgorithm::Multilevel => self.multilevel_partition_with_depth(&graph, 0)?,
            _ => {
                // Default to spectral
                self.spectral_partition(&graph)?
            }
        };

        // Extract subproblems
        let subproblems = self.extract_subproblems(qubo, var_map, &partition_assignment)?;

        // Compute partition metrics
        let metrics = self.compute_partition_metrics(&graph, &partition_assignment);

        let coupling_terms = self.extract_coupling_terms(qubo, &partition_assignment)?;

        Ok(Partitioning {
            partition_assignment,
            subproblems,
            coupling_terms,
            metrics,
        })
    }

    /// Build graph from QUBO matrix
    fn build_graph_from_qubo(&self, qubo: &Array2<f64>) -> Result<Graph, String> {
        let n = qubo.shape()[0];
        let mut edges = Vec::new();
        let mut node_weights = vec![1.0; n];

        for i in 0..n {
            // Node weight from diagonal
            node_weights[i] = qubo[[i, i]].abs();

            for j in i + 1..n {
                if qubo[[i, j]].abs() > 1e-10 {
                    edges.push(Edge {
                        from: i,
                        to: j,
                        weight: qubo[[i, j]].abs(),
                    });
                }
            }
        }

        Ok(Graph {
            num_nodes: n,
            edges,
            node_weights,
        })
    }

    /// Kernighan-Lin partitioning
    fn kernighan_lin_partition(&self, graph: &Graph) -> Result<Vec<usize>, String> {
        let n = graph.num_nodes;
        let mut partition = vec![0; n];

        // Initialize random bisection
        let mut rng = thread_rng();
        for i in 0..n / 2 {
            partition[i] = 1;
        }
        partition.shuffle(&mut rng);

        // Iterative improvement with maximum iterations
        let max_iterations = 100;
        let min_gain_threshold = 1e-10;

        for _iteration in 0..max_iterations {
            // Compute gains for all swaps
            let mut best_swap = None;
            let mut best_gain = 0.0;

            for i in 0..n {
                for j in i + 1..n {
                    if partition[i] != partition[j] {
                        let gain = self.compute_swap_gain(graph, &partition, i, j);
                        if gain > best_gain {
                            best_gain = gain;
                            best_swap = Some((i, j));
                        }
                    }
                }
            }

            if best_gain > min_gain_threshold {
                if let Some((i, j)) = best_swap {
                    // Perform swap
                    let temp = partition[i];
                    partition[i] = partition[j];
                    partition[j] = temp;
                }
            } else {
                break; // No improvement
            }
        }

        // Extend to k-way if needed
        if self.num_partitions > 2 {
            self.extend_to_kway(graph, partition)
        } else {
            Ok(partition)
        }
    }

    /// Compute gain from swapping two nodes
    fn compute_swap_gain(&self, graph: &Graph, partition: &[usize], i: usize, j: usize) -> f64 {
        let mut gain = 0.0;

        // Compute change in edge cut
        for edge in &graph.edges {
            let (u, v) = (edge.from, edge.to);

            if u == i || u == j || v == i || v == j {
                let current_cut = if partition[u] != partition[v] {
                    edge.weight
                } else {
                    0.0
                };

                // Simulate swap
                let mut new_partition = partition.to_vec();
                new_partition[i] = partition[j];
                new_partition[j] = partition[i];

                let new_cut = if new_partition[u] != new_partition[v] {
                    edge.weight
                } else {
                    0.0
                };
                gain += current_cut - new_cut;
            }
        }

        gain
    }

    /// Spectral partitioning using Laplacian eigenvector
    fn spectral_partition(&self, graph: &Graph) -> Result<Vec<usize>, String> {
        let n = graph.num_nodes;

        // Build Laplacian matrix
        let laplacian = self.build_laplacian(graph)?;

        // Find second smallest eigenvector (Fiedler vector)
        let fiedler_vector = self.compute_fiedler_vector(&laplacian)?;

        // Partition based on sign of Fiedler vector
        let mut partition = vec![0; n];
        for i in 0..n {
            partition[i] = if fiedler_vector[i] >= 0.0 { 0 } else { 1 };
        }

        // Extend to k-way if needed
        if self.num_partitions > 2 {
            self.extend_to_kway(graph, partition)
        } else {
            Ok(partition)
        }
    }

    /// Build graph Laplacian matrix
    fn build_laplacian(&self, graph: &Graph) -> Result<Array2<f64>, String> {
        let n = graph.num_nodes;
        let mut laplacian = Array2::zeros((n, n));

        // Add edge weights
        for edge in &graph.edges {
            let (i, j) = (edge.from, edge.to);
            laplacian[[i, j]] = -edge.weight;
            laplacian[[j, i]] = -edge.weight;
        }

        // Add diagonal elements (node degrees)
        for i in 0..n {
            let degree: f64 = graph
                .edges
                .iter()
                .filter(|e| e.from == i || e.to == i)
                .map(|e| e.weight)
                .sum();
            laplacian[[i, i]] = degree;
        }

        Ok(laplacian)
    }

    /// Compute Fiedler vector (second smallest eigenvector)
    fn compute_fiedler_vector(&self, laplacian: &Array2<f64>) -> Result<Array1<f64>, String> {
        let n = laplacian.shape()[0];

        // Simple power iteration for demonstration
        // In practice, would use proper eigenvalue solver
        let mut vector = Array1::from_vec((0..n).map(|i| (i as f64).sin()).collect());

        for _iter in 0..100 {
            // Multiply by Laplacian
            let mut new_vector = Array1::zeros(n);
            for i in 0..n {
                for j in 0..n {
                    new_vector[i] += laplacian[[i, j]] * vector[j];
                }
            }

            // Normalize
            let norm = new_vector.mapv(|x: f64| x * x).sum().sqrt();
            if norm > 1e-10 {
                vector = new_vector / norm;
            }
        }

        Ok(vector)
    }

    /// Multilevel partitioning with recursion depth tracking
    fn multilevel_partition_with_depth(
        &self,
        graph: &Graph,
        depth: usize,
    ) -> Result<Vec<usize>, String> {
        if depth >= self.max_recursion_depth || graph.num_nodes < 10 {
            // Base case: use simple algorithm
            return self.kernighan_lin_partition(graph);
        }

        // Coarsen graph
        let (coarse_graph, mapping) = self.coarsen_graph(graph)?;

        // Recursively partition coarse graph
        let coarse_partition = self.multilevel_partition_with_depth(&coarse_graph, depth + 1)?;

        // Uncoarsen and refine
        let fine_partition = self.uncoarsen_partition(graph, &coarse_partition, &mapping)?;

        Ok(fine_partition)
    }

    /// Coarsen graph by merging strongly connected nodes
    fn coarsen_graph(&self, graph: &Graph) -> Result<(Graph, Vec<usize>), String> {
        let mut mapping = vec![0; graph.num_nodes];
        let mut coarse_weights = Vec::new();
        let mut coarse_edges = HashMap::new();
        let mut num_coarse_nodes = 0;

        // Simple coarsening: merge nodes with strong connections
        let mut visited = vec![false; graph.num_nodes];

        for i in 0..graph.num_nodes {
            if !visited[i] {
                let mut cluster_weight = graph.node_weights[i];
                mapping[i] = num_coarse_nodes;
                visited[i] = true;

                // Find strongly connected neighbors
                for edge in &graph.edges {
                    if edge.from == i && !visited[edge.to] && edge.weight > 0.5 {
                        cluster_weight += graph.node_weights[edge.to];
                        mapping[edge.to] = num_coarse_nodes;
                        visited[edge.to] = true;
                    } else if edge.to == i && !visited[edge.from] && edge.weight > 0.5 {
                        cluster_weight += graph.node_weights[edge.from];
                        mapping[edge.from] = num_coarse_nodes;
                        visited[edge.from] = true;
                    }
                }

                coarse_weights.push(cluster_weight);
                num_coarse_nodes += 1;
            }
        }

        // Build coarse edges
        for edge in &graph.edges {
            let coarse_from = mapping[edge.from];
            let coarse_to = mapping[edge.to];

            if coarse_from != coarse_to {
                *coarse_edges.entry((coarse_from, coarse_to)).or_insert(0.0) += edge.weight;
            }
        }

        let edges = coarse_edges
            .into_iter()
            .map(|((from, to), weight)| Edge { from, to, weight })
            .collect();

        Ok((
            Graph {
                num_nodes: num_coarse_nodes,
                edges,
                node_weights: coarse_weights,
            },
            mapping,
        ))
    }

    /// Uncoarsen partition
    fn uncoarsen_partition(
        &self,
        fine_graph: &Graph,
        coarse_partition: &[usize],
        mapping: &[usize],
    ) -> Result<Vec<usize>, String> {
        let mut fine_partition = vec![0; fine_graph.num_nodes];

        // Project partition
        for (i, &coarse_id) in mapping.iter().enumerate() {
            fine_partition[i] = coarse_partition[coarse_id];
        }

        // Refine
        self.refine_partition(fine_graph, fine_partition)
    }

    /// Refine partition using local search
    fn refine_partition(
        &self,
        graph: &Graph,
        mut partition: Vec<usize>,
    ) -> Result<Vec<usize>, String> {
        let max_refinement_iterations = 10;

        for _iter in 0..max_refinement_iterations {
            let mut improved = false;

            for i in 0..graph.num_nodes {
                let current_part = partition[i];
                let mut best_part = current_part;
                let mut best_gain = 0.0;

                // Try moving to different partitions
                for new_part in 0..self.num_partitions {
                    if new_part != current_part {
                        partition[i] = new_part;
                        let gain =
                            self.compute_node_gain(graph, &partition, i, current_part, new_part);

                        if gain > best_gain {
                            best_gain = gain;
                            best_part = new_part;
                        }
                    }
                }

                if best_part != current_part {
                    partition[i] = best_part;
                    improved = true;
                } else {
                    partition[i] = current_part;
                }
            }

            if !improved {
                break;
            }
        }

        Ok(partition)
    }

    /// Compute gain from moving a node between partitions
    fn compute_node_gain(
        &self,
        graph: &Graph,
        partition: &[usize],
        node: usize,
        old_part: usize,
        new_part: usize,
    ) -> f64 {
        let mut gain = 0.0;

        for edge in &graph.edges {
            if edge.from == node {
                let neighbor_part = partition[edge.to];
                if neighbor_part == old_part {
                    gain -= edge.weight; // Lose internal edge
                } else if neighbor_part == new_part {
                    gain += edge.weight; // Gain internal edge
                }
            } else if edge.to == node {
                let neighbor_part = partition[edge.from];
                if neighbor_part == old_part {
                    gain -= edge.weight; // Lose internal edge
                } else if neighbor_part == new_part {
                    gain += edge.weight; // Gain internal edge
                }
            }
        }

        gain
    }

    /// Extend bisection to k-way partition
    fn extend_to_kway(
        &self,
        graph: &Graph,
        mut partition: Vec<usize>,
    ) -> Result<Vec<usize>, String> {
        if self.num_partitions <= 2 {
            return Ok(partition);
        }

        // Recursive bisection
        for part in 0..self.num_partitions.ilog2() {
            let mut new_partition = partition.clone();

            // Bisect each existing partition
            for p in 0..(1 << part) {
                let nodes: Vec<_> = (0..graph.num_nodes)
                    .filter(|&i| partition[i] == p)
                    .collect();

                if nodes.len() > 1 {
                    // Create subgraph and partition
                    let subgraph = self.extract_subgraph(graph, &nodes)?;
                    let sub_partition = self.kernighan_lin_partition(&subgraph)?;

                    // Map back
                    for (i, &node) in nodes.iter().enumerate() {
                        if sub_partition[i] == 1 {
                            new_partition[node] = p + (1 << part);
                        }
                    }
                }
            }

            partition = new_partition;
        }

        Ok(partition)
    }

    /// Extract subgraph from node set
    fn extract_subgraph(&self, graph: &Graph, nodes: &[usize]) -> Result<Graph, String> {
        let node_map: HashMap<usize, usize> = nodes
            .iter()
            .enumerate()
            .map(|(i, &node)| (node, i))
            .collect();

        let edges = graph
            .edges
            .iter()
            .filter_map(|edge| {
                if let (Some(&from), Some(&to)) = (node_map.get(&edge.from), node_map.get(&edge.to))
                {
                    Some(Edge {
                        from,
                        to,
                        weight: edge.weight,
                    })
                } else {
                    None
                }
            })
            .collect();

        let node_weights = nodes.iter().map(|&i| graph.node_weights[i]).collect();

        Ok(Graph {
            num_nodes: nodes.len(),
            edges,
            node_weights,
        })
    }

    /// Extract subproblems from partition
    fn extract_subproblems(
        &self,
        qubo: &Array2<f64>,
        var_map: &HashMap<String, usize>,
        partition: &[usize],
    ) -> Result<Vec<Subproblem>, String> {
        let mut subproblems = Vec::new();
        let reverse_var_map: HashMap<usize, String> =
            var_map.iter().map(|(k, v)| (*v, k.clone())).collect();

        for part_id in 0..self.num_partitions {
            let var_indices: Vec<_> = partition
                .iter()
                .enumerate()
                .filter(|(_, &p)| p == part_id)
                .map(|(i, _)| i)
                .collect();

            if var_indices.is_empty() {
                continue;
            }

            let variables: Vec<String> = var_indices
                .iter()
                .filter_map(|&i| reverse_var_map.get(&i))
                .cloned()
                .collect();

            // Extract subproblem QUBO
            let sub_size = var_indices.len();
            let mut sub_qubo = Array2::zeros((sub_size, sub_size));

            for (i, &idx_i) in var_indices.iter().enumerate() {
                for (j, &idx_j) in var_indices.iter().enumerate() {
                    sub_qubo[[i, j]] = qubo[[idx_i, idx_j]];
                }
            }

            // Build variable map for subproblem
            let mut sub_var_map = HashMap::new();
            for (i, var) in variables.iter().enumerate() {
                sub_var_map.insert(var.clone(), i);
            }

            subproblems.push(Subproblem {
                id: part_id,
                variables,
                qubo: sub_qubo,
                var_map: sub_var_map,
            });
        }

        Ok(subproblems)
    }

    /// Extract coupling terms between subproblems
    fn extract_coupling_terms(
        &self,
        qubo: &Array2<f64>,
        partition: &[usize],
    ) -> Result<Vec<CouplingTerm>, String> {
        let mut coupling_terms = Vec::new();
        let n = qubo.shape()[0];

        for i in 0..n {
            for j in i + 1..n {
                if partition[i] != partition[j] && qubo[[i, j]].abs() > 1e-10 {
                    coupling_terms.push(CouplingTerm {
                        var1: format!("x{}", i),
                        var2: format!("x{}", j),
                        subproblem1: partition[i],
                        subproblem2: partition[j],
                        weight: qubo[[i, j]],
                    });
                }
            }
        }

        Ok(coupling_terms)
    }

    /// Compute partition quality metrics
    fn compute_partition_metrics(&self, graph: &Graph, partition: &[usize]) -> PartitionMetrics {
        let edge_cut = self.compute_edge_cut(graph, partition);
        let balance = self.compute_balance(graph, partition);
        let modularity = self.compute_modularity(graph, partition);
        let conductance = self.compute_conductance(graph, partition);

        PartitionMetrics {
            edge_cut,
            balance,
            modularity,
            conductance,
        }
    }

    /// Compute edge cut (total weight of edges crossing partitions)
    fn compute_edge_cut(&self, graph: &Graph, partition: &[usize]) -> f64 {
        graph
            .edges
            .iter()
            .filter(|edge| partition[edge.from] != partition[edge.to])
            .map(|edge| edge.weight)
            .sum()
    }

    /// Compute partition balance (how evenly distributed nodes are)
    fn compute_balance(&self, graph: &Graph, partition: &[usize]) -> f64 {
        let mut part_sizes = vec![0; self.num_partitions];
        for &p in partition {
            part_sizes[p] += 1;
        }

        let max_size = *part_sizes.iter().max().unwrap_or(&0) as f64;
        let ideal_size = graph.num_nodes as f64 / self.num_partitions as f64;

        if ideal_size > 0.0 {
            1.0 - (max_size - ideal_size) / ideal_size
        } else {
            1.0
        }
    }

    /// Compute modularity (quality of community structure)
    fn compute_modularity(&self, graph: &Graph, partition: &[usize]) -> f64 {
        let total_weight: f64 = graph.edges.iter().map(|e| e.weight).sum();
        if total_weight == 0.0 {
            return 0.0;
        }

        let mut modularity = 0.0;

        for i in 0..graph.num_nodes {
            for j in 0..graph.num_nodes {
                if partition[i] == partition[j] {
                    let edge_weight = graph
                        .edges
                        .iter()
                        .find(|e| (e.from == i && e.to == j) || (e.from == j && e.to == i))
                        .map(|e| e.weight)
                        .unwrap_or(0.0);

                    let degree_i: f64 = graph
                        .edges
                        .iter()
                        .filter(|e| e.from == i || e.to == i)
                        .map(|e| e.weight)
                        .sum();

                    let degree_j: f64 = graph
                        .edges
                        .iter()
                        .filter(|e| e.from == j || e.to == j)
                        .map(|e| e.weight)
                        .sum();

                    modularity += edge_weight - (degree_i * degree_j) / (2.0 * total_weight);
                }
            }
        }

        modularity / (2.0 * total_weight)
    }

    /// Compute conductance (ratio of edge cut to smallest partition volume)
    fn compute_conductance(&self, graph: &Graph, partition: &[usize]) -> f64 {
        let edge_cut = self.compute_edge_cut(graph, partition);

        let mut part_volumes = vec![0.0; self.num_partitions];
        for edge in &graph.edges {
            part_volumes[partition[edge.from]] += edge.weight;
            part_volumes[partition[edge.to]] += edge.weight;
        }

        let min_volume = part_volumes.iter().cloned().fold(f64::INFINITY, f64::min);

        if min_volume > 0.0 {
            edge_cut / min_volume
        } else {
            f64::INFINITY
        }
    }
}
