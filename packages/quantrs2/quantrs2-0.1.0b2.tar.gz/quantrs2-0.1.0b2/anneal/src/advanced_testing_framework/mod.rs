//! Advanced Testing Infrastructure for Quantum Annealing Systems
//!
//! This module provides a comprehensive testing framework for quantum annealing
//! systems with scenario-based testing, performance regression detection,
//! cross-platform validation, and stress testing capabilities.
//!
//! Key Features:
//! - Scenario-based testing with complex problem generation
//! - Performance regression detection with statistical analysis
//! - Cross-platform validation across multiple quantum hardware platforms
//! - Stress testing with large-scale problem generation
//! - Property-based testing for algorithm correctness
//! - Continuous integration and benchmarking
//! - Test result analytics and visualization
//! - Automated test generation and execution

// Re-export all public types
pub use analytics::*;
pub use config::*;
pub use core::*;
pub use platform_validator::*;
pub use property_tester::*;
pub use regression_detector::*;
pub use scenario_engine::*;
pub use stress_tester::*;
pub use types::*;
pub use utils::*;

// Module declarations
pub mod analytics;
pub mod config;
pub mod core;
pub mod platform_validator;
pub mod property_tester;
pub mod regression_detector;
pub mod scenario_engine;
pub mod stress_tester;
pub mod types;
pub mod utils;

// Common imports for all submodules
pub use std::collections::{HashMap, VecDeque};
pub use std::sync::{Arc, Mutex, RwLock};
pub use std::thread;
pub use std::time::{Duration, Instant};

pub use crate::applications::{ApplicationError, ApplicationResult};
pub use crate::ising::IsingModel;
pub use crate::simulator::{AnnealingParams, AnnealingResult, QuantumAnnealingSimulator};
