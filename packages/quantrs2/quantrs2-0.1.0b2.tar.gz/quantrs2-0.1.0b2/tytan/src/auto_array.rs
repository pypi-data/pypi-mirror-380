//! Automatic conversion of sample results to multi-dimensional arrays.
//!
//! This module provides utilities for converting sample results from
//! quantum annealing to multi-dimensional arrays, which are easier to
//! manipulate and visualize.

// We don't use these imports directly in the non-dwave version
#[cfg(feature = "dwave")]
use scirs2_core::ndarray::{Array, ArrayD, IxDyn};
#[cfg(feature = "dwave")]
use quantrs2_symengine::Expression as SymEngineExpression;
#[cfg(feature = "dwave")]
use regex::Regex;
#[cfg(feature = "dwave")]
use std::collections::HashMap;
use thiserror::Error;

#[cfg(feature = "dwave")]
use crate::sampler::SampleResult;

/// Errors that can occur during array conversion
#[derive(Error, Debug)]
pub enum AutoArrayError {
    /// Error when the format string is invalid
    #[error("Invalid format string: {0}")]
    InvalidFormat(String),

    /// Error when the dimension is unsupported
    #[error("Unsupported dimension: {0}")]
    UnsupportedDimension(usize),

    /// Error when parsing indices
    #[error("Failed to parse indices: {0}")]
    ParseError(String),
}

/// Result type for array conversion operations
pub type AutoArrayResult<T> = Result<T, AutoArrayError>;

/// Automatic converter for quantum annealing results
///
/// This struct provides methods for converting SampleResult objects
/// into multi-dimensional arrays, which are easier to manipulate and visualize.
#[cfg(feature = "dwave")]
pub struct AutoArray<'a> {
    /// The sample result to convert
    result: &'a SampleResult,
}

#[cfg(feature = "dwave")]
impl<'a> AutoArray<'a> {
    /// Create a new automatic array converter
    ///
    /// # Arguments
    ///
    /// * `result` - The sample result to convert
    pub fn new(result: &'a SampleResult) -> Self {
        Self { result }
    }

    /// Convert to an n-dimensional array
    ///
    /// This method converts the sample result to an n-dimensional array
    /// based on the specified format string.
    ///
    /// # Arguments
    ///
    /// * `format` - The format string with {} placeholders for indices
    ///
    /// # Returns
    ///
    /// A tuple containing:
    /// - The n-dimensional array of values
    /// - A vector of indices for each dimension
    pub fn get_ndarray(&self, format: &str) -> AutoArrayResult<(ArrayD<i32>, Vec<Vec<String>>)> {
        // Count the number of dimensions from format placeholders
        let dim_count = format.matches("{}").count();

        if dim_count == 0 {
            return Err(AutoArrayError::InvalidFormat(
                "Format string must contain at least one {} placeholder".to_string(),
            ));
        }

        if dim_count > 5 {
            return Err(AutoArrayError::UnsupportedDimension(dim_count));
        }

        // Create a regex to extract indices
        let re_str = format.replace("{}", "(\\d+|\\w+)");
        #[cfg(feature = "dwave")]
        let re = Regex::new(&re_str)
            .map_err(|e| AutoArrayError::InvalidFormat(format!("Invalid regex: {}", e)))?;

        // Extract all indices from variable names
        let mut indices_by_dim: Vec<Vec<String>> = vec![Vec::new(); dim_count];

        for var_name in self.result.assignments.keys() {
            if let Some(captures) = re.captures(var_name) {
                if captures.len() > 1 {
                    for i in 1..=dim_count {
                        if let Some(m) = captures.get(i) {
                            indices_by_dim[i - 1].push(m.as_str().to_string());
                        }
                    }
                }
            }
        }

        // Deduplicate and sort indices naturally (1, 2, 10 instead of 1, 10, 2)
        for dim_indices in &mut indices_by_dim {
            // Try to parse as numbers for natural sorting
            dim_indices.sort_by(|a, b| {
                match (a.parse::<i32>(), b.parse::<i32>()) {
                    (Ok(na), Ok(nb)) => na.cmp(&nb),
                    _ => a.cmp(b), // Fall back to lexicographic for non-numeric
                }
            });
            dim_indices.dedup();
        }

        // Determine array shape
        let shape: Vec<usize> = indices_by_dim.iter().map(|indices| indices.len()).collect();
        let shape_dim = IxDyn(&shape);

        // Create array filled with -1 (representing missing values)
        let mut array = Array::from_elem(shape_dim, -1);

        // Fill the array with values from the result
        for (var_name, &value) in &self.result.assignments {
            if let Some(captures) = re.captures(var_name) {
                if captures.len() > 1 {
                    // Extract indices
                    let mut index_values = Vec::new();
                    for i in 1..=dim_count {
                        if let Some(m) = captures.get(i) {
                            let idx_str = m.as_str();
                            let dim_indices = &indices_by_dim[i - 1];
                            if let Some(pos) = dim_indices.iter().position(|x| x == idx_str) {
                                index_values.push(pos);
                            }
                        }
                    }

                    // Set array value
                    if index_values.len() == dim_count {
                        let mut idx = IxDyn(&index_values);
                        array[idx] = if value { 1 } else { 0 };
                    }
                }
            }
        }

        Ok((array, indices_by_dim))
    }

    /// Convert to a pandas-like DataFrame
    ///
    /// This method converts the sample result to a 2D array
    /// that can be easily displayed as a table.
    ///
    /// # Arguments
    ///
    /// * `format` - The format string with {} placeholders for indices
    ///
    /// # Returns
    ///
    /// A tuple containing:
    /// - The 2D array of values
    /// - A vector of indices for each dimension
    pub fn get_dframe(
        &self,
        format: &str,
    ) -> AutoArrayResult<(Array<i32, scirs2_core::ndarray::Ix2>, Vec<Vec<String>>)> {
        // Count the number of dimensions from format placeholders
        let dim_count = format.matches("{}").count();

        if dim_count == 0 || dim_count > 2 {
            return Err(AutoArrayError::UnsupportedDimension(dim_count));
        }

        // Get the n-dimensional array
        let (nd_array, indices) = self.get_ndarray(format)?;

        // If 1D, convert to 2D
        if dim_count == 1 {
            let shape = nd_array.shape();
            let mut array = Array::zeros((1, shape[0]));
            for i in 0..shape[0] {
                array[[0, i]] = nd_array[IxDyn(&[i])];
            }
            Ok((array, indices))
        } else {
            // If 2D, convert to Array2
            let shape = nd_array.shape();
            let mut array = Array::zeros((shape[0], shape[1]));
            for i in 0..shape[0] {
                for j in 0..shape[1] {
                    array[[i, j]] = nd_array[IxDyn(&[i, j])];
                }
            }
            Ok((array, indices))
        }
    }

    /// Convert to an image
    ///
    /// This method converts the sample result to a 2D array
    /// that can be displayed as an image.
    ///
    /// # Arguments
    ///
    /// * `format` - The format string with {} placeholders for indices
    ///
    /// # Returns
    ///
    /// A tuple containing:
    /// - The 2D array of values (0 or 255)
    /// - A vector of indices for each dimension
    pub fn get_image(
        &self,
        format: &str,
    ) -> AutoArrayResult<(Array<u8, scirs2_core::ndarray::Ix2>, Vec<Vec<String>>)> {
        // Count the number of dimensions from format placeholders
        let dim_count = format.matches("{}").count();

        if dim_count != 2 {
            return Err(AutoArrayError::UnsupportedDimension(dim_count));
        }

        // Get the 2D array
        let (array, indices) = self.get_dframe(format)?;

        // Convert to u8 image (0 or 255)
        let mut image = Array::zeros(array.dim());
        for i in 0..array.shape()[0] {
            for j in 0..array.shape()[1] {
                image[[i, j]] = if array[[i, j]] > 0 { 255 } else { 0 };
            }
        }

        Ok((image, indices))
    }

    /// Get the value of an n-bit encoded variable
    ///
    /// This method calculates the value of an n-bit encoded variable
    /// from the sample result.
    ///
    /// # Arguments
    ///
    /// * `expr` - The symbolic expression representing the n-bit variable
    ///
    /// # Returns
    ///
    /// The calculated value of the n-bit variable
    #[cfg(feature = "dwave")]
    pub fn get_nbit_value(&self, expr: &SymEngineExpression) -> AutoArrayResult<f64> {
        // TODO: Implement n-bit value calculation
        // This will require evaluating the symbolic expression with
        // the sample values substituted in.

        // For now, return a placeholder
        Ok(0.0)
    }
}
