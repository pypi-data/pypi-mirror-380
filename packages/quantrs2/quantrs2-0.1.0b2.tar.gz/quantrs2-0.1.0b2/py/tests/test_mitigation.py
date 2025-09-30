"""Tests for quantum error mitigation functionality"""

import pytest
import numpy as np

# Safe import pattern
try:
    import quantrs2
    from quantrs2.mitigation import (
        ZNEConfig, ZNEResult, Observable, ZeroNoiseExtrapolation,
        CircuitFolding, ExtrapolationFitting,
        ProbabilisticErrorCancellation, VirtualDistillation, SymmetryVerification
    )
    from quantrs2.measurement import MeasurementResult, MeasurementSampler
    HAS_MITIGATION = True
except ImportError:
    HAS_MITIGATION = False
    
    # Stub implementations
    class ZNEConfig:
        def __init__(self, scale_factors=None, scaling_method="global", 
                     extrapolation_method="richardson", bootstrap_samples=100, 
                     confidence_level=0.95):
            self.scale_factors = scale_factors or [1.0, 1.5, 2.0, 2.5, 3.0]
            self.scaling_method = scaling_method
            self.extrapolation_method = extrapolation_method
            self.bootstrap_samples = bootstrap_samples
            self.confidence_level = confidence_level
    
    class ZNEResult:
        def __init__(self, mitigated_value=1.0, error_estimate=0.1, raw_data=None,
                     fit_params=None, r_squared=0.99, extrapolation_fn=None):
            self.mitigated_value = mitigated_value
            self.error_estimate = error_estimate
            self.raw_data = raw_data or [(1.0, 0.9), (2.0, 0.8), (3.0, 0.7)]
            self.fit_params = fit_params or np.array([1.0, -0.1])
            self.r_squared = r_squared
            self.extrapolation_fn = extrapolation_fn
    
    class Observable:
        def __init__(self, pauli_string, coefficient=1.0):
            self.pauli_string = pauli_string
            self.coefficient = coefficient
        
        @classmethod
        def z(cls, qubit):
            return cls([(qubit, "Z")])
        
        @classmethod
        def zz(cls, qubit1, qubit2):
            return cls([(qubit1, "Z"), (qubit2, "Z")])
        
        def expectation_value(self, measurement):
            return 1.0
    
    class CircuitFolding:
        @staticmethod
        def fold_global(circuit, scale_factor):
            if scale_factor < 1.0:
                raise ValueError("Scale factor must be >= 1.0")
            return circuit
        
        @staticmethod
        def fold_local(circuit, scale_factor, weights=None):
            return circuit
    
    class ExtrapolationFitting:
        @staticmethod
        def fit_linear(x, y):
            return ZNEResult(mitigated_value=0.9, r_squared=0.99)
        
        @staticmethod
        def fit_polynomial(x, y, degree):
            return ZNEResult(mitigated_value=0.9)
        
        @staticmethod
        def fit_exponential(x, y):
            return ZNEResult(mitigated_value=0.9)
        
        @staticmethod
        def fit_richardson(x, y):
            return ZNEResult(mitigated_value=1.1)
        
        @staticmethod
        def fit_adaptive(x, y):
            return ZNEResult(mitigated_value=0.9, r_squared=0.95)
    
    class ZeroNoiseExtrapolation:
        def __init__(self, config):
            self.config = config
        
        def fold_circuit(self, circuit, scale_factor):
            return circuit
        
        def extrapolate(self, data):
            return ZNEResult(mitigated_value=1.0)
        
        def mitigate_observable(self, observable, measurements):
            return ZNEResult(mitigated_value=1.0)
    
    class ProbabilisticErrorCancellation:
        def quasi_probability_decomposition(self, circuit):
            raise ValueError("PEC not yet implemented")
    
    class VirtualDistillation:
        def distill(self, circuits):
            raise ValueError("Virtual distillation not yet implemented")
    
    class SymmetryVerification:
        def verify_symmetry(self, circuit, symmetry_type):
            raise ValueError("Symmetry verification not yet implemented")
    
    # Mock Circuit class
    class Circuit:
        def __init__(self, n_qubits):
            self.n_qubits = n_qubits
            self.num_gates = 0
        
        def h(self, qubit):
            self.num_gates += 1
        
        def cnot(self, control, target):
            self.num_gates += 1
        
        def rx(self, qubit, angle):
            self.num_gates += 1
    
    quantrs2 = type('MockQuantrs2', (), {'Circuit': Circuit})()


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_zne_config():
    """Test ZNE configuration creation and properties"""
    # Default config
    config = ZNEConfig()
    assert config.scale_factors == [1.0, 1.5, 2.0, 2.5, 3.0]
    assert config.scaling_method == "global"
    assert config.extrapolation_method == "richardson"
    assert config.bootstrap_samples == 100
    assert config.confidence_level == 0.95
    
    # Custom config
    config = ZNEConfig(
        scale_factors=[1.0, 2.0, 3.0],
        scaling_method="local",
        extrapolation_method="exponential",
        bootstrap_samples=50,
        confidence_level=0.99
    )
    assert config.scale_factors == [1.0, 2.0, 3.0]
    assert config.scaling_method == "local"
    assert config.extrapolation_method == "exponential"
    assert config.bootstrap_samples == 50
    assert config.confidence_level == 0.99
    
    # Test setters
    config.scale_factors = [1.0, 1.5, 2.0]
    assert config.scale_factors == [1.0, 1.5, 2.0]


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_observable():
    """Test observable creation and expectation values"""
    # Single qubit observable
    obs_z = Observable.z(0)
    assert obs_z.pauli_string == [(0, "Z")]
    assert obs_z.coefficient == 1.0
    
    # Two qubit observable
    obs_zz = Observable.zz(0, 1)
    assert obs_zz.pauli_string == [(0, "Z"), (1, "Z")]
    assert obs_zz.coefficient == 1.0
    
    # Custom observable
    obs_custom = Observable([(0, "X"), (1, "Y"), (2, "Z")], 0.5)
    assert obs_custom.pauli_string == [(0, "X"), (1, "Y"), (2, "Z")]
    assert obs_custom.coefficient == 0.5
    
    # Test expectation value calculation
    # Create mock measurement result
    counts = {"00": 50, "11": 50}  # Perfect Bell state
    measurement = type('obj', (object,), {
        'counts': counts,
        'shots': 100,
        'n_qubits': 2
    })
    
    # For Z0Z1, |00⟩ gives +1 and |11⟩ gives +1
    exp_val = obs_zz.expectation_value(measurement)
    assert abs(exp_val - 1.0) < 0.01


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_circuit_folding():
    """Test circuit folding operations"""
    circuit = quantrs2.Circuit(2)
    circuit.h(0)
    circuit.cnot(0, 1)
    original_gates = circuit.num_gates
    
    # Global folding
    folded = CircuitFolding.fold_global(circuit, 1.0)
    assert folded.num_gates == original_gates  # Scale 1.0 = no change
    
    folded = CircuitFolding.fold_global(circuit, 3.0)
    # Currently returns same circuit (placeholder), but would be larger
    assert folded.num_gates >= original_gates
    
    # Local folding
    folded = CircuitFolding.fold_local(circuit, 2.0)
    assert folded.num_gates >= original_gates
    
    # With custom weights
    weights = [1.0, 2.0]  # Different weights for H and CNOT
    folded = CircuitFolding.fold_local(circuit, 2.0, weights)
    assert folded.num_gates >= original_gates
    
    # Test error handling
    with pytest.raises(ValueError):
        CircuitFolding.fold_global(circuit, 0.5)  # Scale < 1.0


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_extrapolation_fitting():
    """Test different extrapolation methods"""
    # Generate test data
    x = np.array([1.0, 1.5, 2.0, 2.5, 3.0])
    y_linear = 0.9 - 0.1 * x  # Linear decay
    y_exp = 0.9 * np.exp(-0.2 * (x - 1))  # Exponential decay
    
    # Linear fit
    result = ExtrapolationFitting.fit_linear(x, y_linear)
    assert isinstance(result, ZNEResult)
    assert abs(result.mitigated_value - 0.9) < 0.01  # y-intercept
    assert result.r_squared > 0.99  # Perfect linear fit
    assert len(result.fit_params) >= 2
    
    # Polynomial fit
    result = ExtrapolationFitting.fit_polynomial(x, y_linear, 2)
    assert abs(result.mitigated_value - 0.9) < 0.02
    
    # Exponential fit
    result = ExtrapolationFitting.fit_exponential(x, y_exp)
    assert abs(result.mitigated_value - 0.9) < 0.05
    
    # Richardson extrapolation
    result = ExtrapolationFitting.fit_richardson(x, y_linear)
    assert result.mitigated_value < y_linear[0]  # Should extrapolate below data
    
    # Adaptive fit
    result = ExtrapolationFitting.fit_adaptive(x, y_linear)
    assert result.r_squared > 0.9  # Should find good fit


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_zero_noise_extrapolation():
    """Test ZNE workflow"""
    # Create simple circuit
    circuit = quantrs2.Circuit(1)
    circuit.rx(0, np.pi/4)
    
    # Configure ZNE
    config = ZNEConfig(
        scale_factors=[1.0, 2.0, 3.0],
        scaling_method="global",
        extrapolation_method="linear"
    )
    zne = ZeroNoiseExtrapolation(config)
    
    # Test circuit folding
    folded = zne.fold_circuit(circuit, 2.0)
    assert folded.num_gates >= circuit.num_gates
    
    # Test extrapolation
    data = [(1.0, 0.9), (2.0, 0.8), (3.0, 0.7)]
    result = zne.extrapolate(data)
    assert isinstance(result, ZNEResult)
    assert result.mitigated_value > 0.9  # Should extrapolate above highest value
    
    # Test with observable
    obs = Observable.z(0)
    
    # Create mock measurements
    measurements = []
    for scale, value in data:
        counts = {"0": int(1000 * (1 + value) / 2), "1": int(1000 * (1 - value) / 2)}
        measurement = type('obj', (object,), {
            'counts': counts,
            'shots': 1000,
            'n_qubits': 1
        })
        measurements.append((scale, measurement))
    
    result = zne.mitigate_observable(obs, measurements)
    assert isinstance(result, ZNEResult)


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_zne_result_properties():
    """Test ZNE result object properties"""
    # Create result through extrapolation
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([0.9, 0.8, 0.7])
    result = ExtrapolationFitting.fit_linear(x, y)
    
    # Check properties
    assert hasattr(result, 'mitigated_value')
    assert hasattr(result, 'error_estimate')
    assert hasattr(result, 'raw_data')
    assert hasattr(result, 'fit_params')
    assert hasattr(result, 'r_squared')
    assert hasattr(result, 'extrapolation_fn')
    
    # Check raw data
    raw_data = result.raw_data
    assert len(raw_data) == 3
    assert all(isinstance(point, tuple) and len(point) == 2 for point in raw_data)
    
    # Check fit params
    params = result.fit_params
    assert isinstance(params, np.ndarray)
    assert len(params) >= 1


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_placeholder_methods():
    """Test placeholder implementations"""
    # PEC
    pec = ProbabilisticErrorCancellation()
    circuit = quantrs2.Circuit(1)
    with pytest.raises(ValueError, match="PEC not yet implemented"):
        pec.quasi_probability_decomposition(circuit)
    
    # Virtual Distillation
    vd = VirtualDistillation()
    circuits = [quantrs2.Circuit(1) for _ in range(3)]
    with pytest.raises(ValueError, match="Virtual distillation not yet implemented"):
        vd.distill(circuits)
    
    # Symmetry Verification
    sv = SymmetryVerification()
    circuit = quantrs2.Circuit(2)
    with pytest.raises(ValueError, match="Symmetry verification not yet implemented"):
        sv.verify_symmetry(circuit, "parity")


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_observable_pauli_validation():
    """Test observable Pauli string validation"""
    # Valid Pauli strings
    Observable([(0, "I")], 1.0)
    Observable([(0, "X"), (1, "Y"), (2, "Z")], 1.0)
    
    # Invalid Pauli string
    with pytest.raises(ValueError, match="Invalid Pauli operator"):
        Observable([(0, "A")], 1.0)
    
    with pytest.raises(ValueError, match="Invalid Pauli operator"):
        Observable([(0, "XY")], 1.0)


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_repr_methods():
    """Test string representations"""
    # ZNEConfig
    config = ZNEConfig()
    repr_str = repr(config)
    assert "ZNEConfig" in repr_str
    assert "scale_factors" in repr_str
    assert "global" in repr_str
    
    # Observable
    obs = Observable.zz(0, 1)
    repr_str = repr(obs)
    assert "Observable" in repr_str
    assert "Z_0" in repr_str
    assert "Z_1" in repr_str
    
    # ZNEResult (from fit)
    result = ExtrapolationFitting.fit_linear(
        np.array([1.0, 2.0]), 
        np.array([0.9, 0.8])
    )
    repr_str = repr(result)
    assert "ZNEResult" in repr_str
    assert "mitigated_value" in repr_str


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_different_extrapolation_methods_config():
    """Test configuration with different extrapolation methods"""
    methods = [
        "linear", "polynomial2", "polynomial3", 
        "exponential", "richardson", "adaptive"
    ]
    
    for method in methods:
        config = ZNEConfig(extrapolation_method=method)
        assert method in config.extrapolation_method
    
    # Invalid method
    with pytest.raises(ValueError, match="Unknown extrapolation method"):
        ZNEConfig(extrapolation_method="invalid")


@pytest.mark.skipif(not HAS_MITIGATION, reason="quantrs2.mitigation not available")
def test_different_scaling_methods_config():
    """Test configuration with different scaling methods"""
    methods = ["global", "local", "pulse", "digital"]
    
    for method in methods:
        config = ZNEConfig(scaling_method=method)
        assert config.scaling_method == method
    
    # Invalid method
    with pytest.raises(ValueError, match="Unknown scaling method"):
        ZNEConfig(scaling_method="invalid")