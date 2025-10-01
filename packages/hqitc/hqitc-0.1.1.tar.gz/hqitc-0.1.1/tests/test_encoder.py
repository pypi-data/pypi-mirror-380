"""Tests for the quantum encoder functionality."""

import numpy as np
import pytest
from hqitc.encoder import QuantumInspiredEncoder


class TestQuantumInspiredEncoder:
    """Test quantum-inspired encoding functionality."""

    @pytest.fixture
    def encoder(self):
        """Create QuantumInspiredEncoder instance."""
        return QuantumInspiredEncoder(patch_size=8, quantum_dim=32, seed=42)

    @pytest.fixture
    def test_patches(self):
        """Create test patches for encoding."""
        # Create patches with different characteristics
        patches = []
        
        # Uniform patch
        patches.append(np.full(64, 128.0))
        
        # Gradient patch
        patches.append(np.linspace(0, 255, 64))
        
        # Random patch
        np.random.seed(42)
        patches.append(np.random.randn(64) * 50 + 128)
        
        # Edge patch
        edge_patch = np.concatenate([np.full(32, 50), np.full(32, 200)])
        patches.append(edge_patch)
        
        return np.array(patches)

    def test_initialization(self, encoder):
        """Test QuantumInspiredEncoder initialization."""
        assert encoder.quantum_dim == 32
        assert encoder.patch_size == 8
        assert encoder.amplitude_weights.shape == (64, 32)
        assert encoder.phase_weights.shape == (64, 32)
        assert encoder.reconstruction_weights.shape == (64, 64)  # (quantum_dim*2, patch_dim)
        
        # Check that weights are reasonable
        assert np.std(encoder.amplitude_weights) > 0  # Should have variation
        assert np.std(encoder.phase_weights) > 0
        assert np.std(encoder.reconstruction_weights) > 0

    def test_encode_patches_basic_functionality(self, encoder, test_patches):
        """Test basic encoding functionality."""
        reconstructed = encoder.encode_patches(test_patches)
        
        # Should produce reconstructed patches with same shape
        assert reconstructed.shape == test_patches.shape
        assert reconstructed.dtype == np.float64
        
        # All values should be finite and in valid range
        assert np.all(np.isfinite(reconstructed))
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 255)

    def test_unitary_matrix_creation(self, encoder):
        """Test unitary matrix creation."""
        U = encoder.create_unitary_matrix()
        
        # Should be square with correct dimensions
        assert U.shape == (encoder.quantum_dim, encoder.quantum_dim)
        assert U.dtype == np.complex128
        
        # Should be approximately unitary (U @ U.conj().T ≈ I)
        identity_approx = U @ U.conj().T
        identity = np.eye(encoder.quantum_dim)
        np.testing.assert_allclose(identity_approx, identity, atol=1e-10)

    def test_encode_patches_consistency(self, encoder):
        """Test encode-decode consistency."""
        # Test with different input patterns
        test_inputs = [
            np.zeros((1, 64)),           # All zeros
            np.ones((1, 64)) * 128,      # Uniform gray
            np.linspace(0, 255, 64).reshape(1, -1), # Linear gradient
            np.random.randn(1, 64) * 50 + 128  # Random
        ]
        
        for test_input in test_inputs:
            # Ensure valid input range
            test_input = np.clip(test_input, 0, 255)
            
            # Process patches
            reconstructed = encoder.encode_patches(test_input)
            
            # Should maintain basic properties
            assert reconstructed.shape == test_input.shape
            assert np.all(np.isfinite(reconstructed))
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 255)

    def test_encoding_with_different_quantum_dimensions(self):
        """Test encoding with different quantum dimensions."""
        quantum_dims = [8, 16, 32, 64]
        test_patch = np.random.randn(1, 64) * 50 + 128
        test_patch = np.clip(test_patch, 0, 255)
        
        for dim in quantum_dims:
            encoder = QuantumInspiredEncoder(patch_size=8, quantum_dim=dim, seed=42)
            
            # Should work with any reasonable quantum dimension
            reconstructed = encoder.encode_patches(test_patch)
            
            assert reconstructed.shape == test_patch.shape
            assert np.all(np.isfinite(reconstructed))
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 255)

    def test_batch_processing(self, encoder):
        """Test processing of different batch sizes."""
        patch_size = 64
        
        for batch_size in [1, 5, 10, 20]:
            test_batch = np.random.randn(batch_size, patch_size) * 50 + 128
            test_batch = np.clip(test_batch, 0, 255)  # Ensure valid input range
            
            reconstructed = encoder.encode_patches(test_batch)
            
            assert reconstructed.shape == (batch_size, patch_size)
            assert np.all(np.isfinite(reconstructed))
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 255)

    def test_deterministic_behavior(self, encoder, test_patches):
        """Test that encoding is deterministic."""
        test_patches = np.clip(test_patches, 0, 255)  # Ensure valid range
        
        # Encode same patches multiple times
        results = []
        for _ in range(3):
            reconstructed = encoder.encode_patches(test_patches)
            results.append(reconstructed.copy())
        
        # All results should be identical
        for i in range(1, len(results)):
            np.testing.assert_allclose(results[0], results[i], rtol=1e-14)

    def test_extreme_input_values(self, encoder):
        """Test encoding with extreme input values."""
        extreme_inputs = [
            np.full((1, 64), 0),      # All zeros
            np.full((1, 64), 255),    # All max values
            np.concatenate([np.full((1, 32), 0), np.full((1, 32), 255)], axis=1)  # Sharp contrast
        ]
        
        for extreme_input in extreme_inputs:
            # Should handle without numerical issues
            reconstructed = encoder.encode_patches(extreme_input)
            
            assert np.all(np.isfinite(reconstructed))
            assert reconstructed.shape == extreme_input.shape
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 255)


class TestQuantumEncoderEdgeCases:
    """Test edge cases for quantum encoder."""

    def test_single_patch_encoding(self):
        """Test encoding of single patch."""
        encoder = QuantumInspiredEncoder(patch_size=8, quantum_dim=16, seed=42)
        single_patch = np.random.randn(1, 64) * 50 + 128
        single_patch = np.clip(single_patch, 0, 255)
        
        reconstructed = encoder.encode_patches(single_patch)
        
        assert reconstructed.shape == (1, 64)
        assert np.all(np.isfinite(reconstructed))

    def test_different_patch_sizes(self):
        """Test with different patch sizes."""
        patch_sizes = [4, 8, 16]
        
        for patch_size in patch_sizes:
            patch_dim = patch_size * patch_size
            encoder = QuantumInspiredEncoder(patch_size=patch_size, quantum_dim=32, seed=42)
            test_input = np.random.randn(3, patch_dim) * 50 + 128
            test_input = np.clip(test_input, 0, 255)
            
            reconstructed = encoder.encode_patches(test_input)
            
            assert reconstructed.shape == (3, patch_dim)
            assert np.all(np.isfinite(reconstructed))

    def test_numerical_stability(self):
        """Test numerical stability with various inputs."""
        encoder = QuantumInspiredEncoder(patch_size=8, quantum_dim=32, seed=42)
        
        # Test with edge values
        edge_inputs = [
            np.full((1, 64), 1e-6),   # Very small values
            np.full((1, 64), 255.0),  # Max values
            np.zeros((1, 64)),        # Zero values
        ]
        
        for edge_input in edge_inputs:
            reconstructed = encoder.encode_patches(edge_input)
            
            assert np.all(np.isfinite(reconstructed))
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 255)