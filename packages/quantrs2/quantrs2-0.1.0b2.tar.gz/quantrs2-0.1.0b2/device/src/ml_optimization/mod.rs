//! ML-Driven Circuit Optimization and Hardware Prediction with SciRS2
//!
//! This module provides comprehensive machine learning-driven circuit optimization
//! and hardware performance prediction using SciRS2's advanced ML capabilities,
//! statistical analysis, and optimization algorithms for intelligent quantum computing.

use std::collections::{BTreeMap, HashMap, HashSet, VecDeque};
use std::f64::consts::PI;
use std::sync::{Arc, Mutex, RwLock};
use std::time::{Duration, Instant};

use quantrs2_circuit::prelude::*;
use quantrs2_core::{
    error::{QuantRS2Error, QuantRS2Result},
    gate::GateOp,
    qubit::QubitId,
};

// SciRS2 dependencies are conditionally re-exported through fallback_scirs2

// Fallback implementations when SciRS2 is not available
pub mod fallback_scirs2;
pub use fallback_scirs2::*;

use scirs2_core::ndarray::{s, Array1, Array2, Array3, Array4, ArrayView1, ArrayView2, Axis};
use scirs2_core::Complex64;
use scirs2_core::random::prelude::*;
use tokio::sync::{broadcast, mpsc};

use crate::{
    adaptive_compilation::AdaptiveCompilationConfig,
    backend_traits::{query_backend_capabilities, BackendCapabilities},
    calibration::{CalibrationManager, DeviceCalibration},
    integrated_device_manager::IntegratedQuantumDeviceManager,
    noise_model::CalibrationNoiseModel,
    topology::HardwareTopology,
    CircuitResult, DeviceError, DeviceResult,
};

// Module declarations
pub mod config;
pub mod ensemble;
pub mod features;
pub mod hardware;
pub mod monitoring;
pub mod online_learning;
pub mod optimization;
pub mod training;
pub mod transfer_learning;
pub mod validation;

#[cfg(not(feature = "scirs2"))]
pub mod fallback;

// Re-exports for public API
pub use config::*;
pub use ensemble::*;
pub use features::*;
pub use hardware::*;
pub use monitoring::*;
pub use online_learning::*;
pub use optimization::*;
pub use training::*;
pub use transfer_learning::*;
pub use validation::*;

#[cfg(not(feature = "scirs2"))]
pub use fallback::*;

// TODO: Add implementation functions and types that were in the original file
// This would include the MLOptimizer struct and its implementation
// For now, this refactoring focuses on organizing the configuration types
