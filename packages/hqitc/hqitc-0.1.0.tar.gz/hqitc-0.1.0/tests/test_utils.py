"""Tests for the attention mechanisms and utilities."""

import numpy as np
import pytest
from hqitc.utils import AttentionWaveletTransform, AdaptiveNeuralEntropyCoder


class TestAttentionWaveletTransform:
    """Test attention mechanism functionality."""

    @pytest.fixture
    def attention_mechanism(self):
        """Create AttentionWaveletTransform instance."""
        return AttentionWaveletTransform(embed_dim=64, num_heads=8, seed=42)

    @pytest.fixture  
    def test_patches(self):
        """Create test patches with different characteristics."""
        # Patch 1: Uniform (low importance)
        uniform_patch = np.full(64, 128.0)
        
        # Patch 2: High variance (high importance)
        np.random.seed(42)
        varying_patch = np.random.randn(64) * 50 + 128
        
        # Patch 3: Edge-like pattern (medium-high importance)
        edge_patch = np.concatenate([np.full(32, 50), np.full(32, 200)])
        
        # Patch 4: Periodic pattern 
        periodic_patch = np.sin(np.linspace(0, 4*np.pi, 64)) * 100 + 128
        
        return np.array([uniform_patch, varying_patch, edge_patch, periodic_patch])

    def test_initialization(self, attention_mechanism):
        """Test AttentionWaveletTransform initialization."""
        assert attention_mechanism.embed_dim == 64
        assert attention_mechanism.num_heads == 8
        assert attention_mechanism.head_dim == 8  # 64 // 8
        
        # Check weight matrices have correct shapes
        assert attention_mechanism.query_weights.shape == (64, 64)
        assert attention_mechanism.key_weights.shape == (64, 64)
        assert attention_mechanism.value_weights.shape == (64, 64)

    def test_layer_norm(self, attention_mechanism):
        """Test layer normalization functionality."""
        # Create test data with known statistics
        test_data = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
        normalized = attention_mechanism.layer_norm(test_data)
        
        # Check that each row is normalized
        assert normalized.shape == test_data.shape
        
        # Each row should have approximately zero mean and unit variance
        for i in range(normalized.shape[0]):
            row_mean = np.mean(normalized[i])
            row_var = np.var(normalized[i])
            assert abs(row_mean) < 1e-5
            assert abs(row_var - 1.0) < 1e-5

    def test_softmax(self, attention_mechanism):
        """Test softmax implementation."""
        test_data = np.array([[1, 2, 3], [10, 20, 30]])
        softmax_result = attention_mechanism.softmax(test_data)
        
        # Check properties of softmax
        assert softmax_result.shape == test_data.shape
        assert np.all(softmax_result >= 0)
        assert np.all(softmax_result <= 1)
        
        # Each row should sum to 1
        row_sums = np.sum(softmax_result, axis=1)
        np.testing.assert_allclose(row_sums, 1.0, atol=1e-10)

    def test_multi_head_attention_output_shape(self, attention_mechanism, test_patches):
        """Test that multi-head attention produces correct output shapes."""
        attended_patches, importance = attention_mechanism.multi_head_attention(test_patches)
        
        # Output patches should match input shape
        assert attended_patches.shape == test_patches.shape
        
        # Importance should be one value per patch
        assert importance.shape == (test_patches.shape[0],)

    def test_attention_importance_ranking(self, attention_mechanism, test_patches):
        """Test that attention correctly ranks patch importance."""
        _, importance = attention_mechanism.multi_head_attention(test_patches)
        
        # All importance scores should be valid
        assert np.all(importance >= 0)
        assert np.all(importance <= 1)
        
        # Varying patch should have higher importance than uniform patch
        uniform_idx = 0
        varying_idx = 1
        assert importance[varying_idx] >= importance[uniform_idx]

    def test_attention_consistency(self, attention_mechanism, test_patches):
        """Test that attention produces consistent results."""
        # Run attention multiple times
        results = []
        for _ in range(3):
            attended, importance = attention_mechanism.multi_head_attention(test_patches)
            results.append((attended.copy(), importance.copy()))
        
        # Results should be identical (deterministic)
        for i in range(1, len(results)):
            np.testing.assert_allclose(results[0][0], results[i][0], rtol=1e-10)
            np.testing.assert_allclose(results[0][1], results[i][1], rtol=1e-10)

    def test_attention_with_different_embed_dims(self):
        """Test attention mechanism with different embedding dimensions."""
        for embed_dim in [16, 32, 64, 128]:
            attention = AttentionWaveletTransform(embed_dim=embed_dim, num_heads=4, seed=42)
            
            # Create patches matching the embedding dimension
            test_patches = np.random.randn(10, embed_dim) * 50 + 128
            
            attended, importance = attention.multi_head_attention(test_patches)
            
            assert attended.shape == test_patches.shape
            assert importance.shape == (10,)

    def test_wavelet_transform_2d(self, attention_mechanism):
        """Test 2D wavelet (DCT) transform."""
        # Create test image
        test_image = np.random.randn(8, 8) * 50 + 128
        
        # Forward transform
        coeffs = attention_mechanism.wavelet_transform_2d(test_image)
        assert coeffs.shape == test_image.shape
        
        # Inverse transform
        reconstructed = attention_mechanism.inverse_wavelet_transform_2d(coeffs)
        assert reconstructed.shape == test_image.shape
        
        # Should be nearly perfect reconstruction
        np.testing.assert_allclose(reconstructed, test_image, atol=1e-10)

    def test_adaptive_coefficient_selection(self, attention_mechanism):
        """Test adaptive coefficient selection."""
        # Create test coefficients with known structure
        coeffs = np.zeros((8, 8))
        coeffs[0, 0] = 100  # DC component (should be kept)
        coeffs[0, 1] = 50   # Low frequency (should be kept)
        coeffs[7, 7] = 10   # High frequency (might be discarded)
        
        # Create attention map that prioritizes low frequencies
        attention_map = np.ones((8, 8))
        attention_map[0, 0] = 1.0  # High importance for DC
        attention_map[0, 1] = 0.8  # Medium importance  
        attention_map[7, 7] = 0.1  # Low importance for high freq
        
        selected_coeffs, indices = attention_mechanism.adaptive_coefficient_selection(
            coeffs, attention_map, keep_ratio=0.5
        )
        
        assert selected_coeffs.shape == coeffs.shape
        
        # DC component should definitely be kept
        assert selected_coeffs[0, 0] == coeffs[0, 0]


class TestAdaptiveNeuralEntropyCoder:
    """Test entropy estimation functionality."""

    @pytest.fixture
    def entropy_coder(self):
        """Create AdaptiveNeuralEntropyCoder instance."""
        return AdaptiveNeuralEntropyCoder(seed=42)

    def test_entropy_estimation_empty(self, entropy_coder):
        """Test entropy estimation with no coefficients."""
        empty_coeffs = np.zeros((10, 10))
        
        entropy_info = entropy_coder.estimate_bits(empty_coeffs)
        
        assert 'total_bits' in entropy_info
        assert 'num_nonzero' in entropy_info
        assert 'bits_per_coeff' in entropy_info
        
        assert entropy_info['num_nonzero'] == 0
        assert entropy_info['total_bits'] > 0  # Small overhead

    def test_entropy_estimation_single_value(self, entropy_coder):
        """Test entropy estimation with single coefficient."""
        single_coeff = np.zeros((5, 5))
        single_coeff[0, 0] = 10
        
        entropy_info = entropy_coder.estimate_bits(single_coeff)
        
        assert entropy_info['num_nonzero'] == 1
        assert entropy_info['total_bits'] > 0
        assert entropy_info['bits_per_coeff'] >= 1

    def test_entropy_estimation_scaling(self, entropy_coder):
        """Test that entropy estimation scales reasonably."""
        # Create coefficients with different ranges
        small_coeffs = np.random.randint(-10, 11, (5, 5))
        large_coeffs = np.random.randint(-1000, 1001, (5, 5))
        
        small_info = entropy_coder.estimate_bits(small_coeffs)
        large_info = entropy_coder.estimate_bits(large_coeffs)
        
        # Larger coefficient values should require more bits
        if large_info['num_nonzero'] > 0 and small_info['num_nonzero'] > 0:
            assert large_info['bits_per_coeff'] >= small_info['bits_per_coeff']

    def test_entropy_estimation_sparsity(self, entropy_coder):
        """Test entropy estimation with different sparsity levels."""
        dense_coeffs = np.random.randint(-50, 51, (10, 10))
        
        # Create sparse version (zero out 80% of coefficients)
        sparse_coeffs = dense_coeffs.copy()
        mask = np.random.rand(10, 10) < 0.8
        sparse_coeffs[mask] = 0
        
        dense_info = entropy_coder.estimate_bits(dense_coeffs)
        sparse_info = entropy_coder.estimate_bits(sparse_coeffs)
        
        # Sparse should have fewer nonzero coefficients
        assert sparse_info['num_nonzero'] <= dense_info['num_nonzero']
        
        # If sparse has coefficients, total bits should be less
        if sparse_info['num_nonzero'] > 0:
            assert sparse_info['total_bits'] <= dense_info['total_bits']

    def test_entropy_estimation_consistency(self, entropy_coder):
        """Test that entropy estimation is consistent."""
        test_coeffs = np.random.randint(-100, 101, (8, 8))
        
        # Estimate multiple times
        results = []
        for _ in range(5):
            info = entropy_coder.estimate_bits(test_coeffs)
            results.append(info)
        
        # All results should be identical
        for i in range(1, len(results)):
            assert results[0]['total_bits'] == results[i]['total_bits']
            assert results[0]['num_nonzero'] == results[i]['num_nonzero']
            assert results[0]['bits_per_coeff'] == results[i]['bits_per_coeff']


class TestUtilsIntegration:
    """Test integration between different utility components."""

    def test_attention_with_entropy_estimation(self):
        """Test combining attention mechanism with entropy estimation."""
        attention = AttentionWaveletTransform(embed_dim=64, num_heads=4, seed=42)
        entropy_coder = AdaptiveNeuralEntropyCoder(seed=42)
        
        # Create test patches
        patches = np.random.randn(20, 64) * 50 + 128
        
        # Apply attention
        attended_patches, importance = attention.multi_head_attention(patches)
        
        # Reshape to 2D for coefficient selection
        coeffs_2d = attended_patches.reshape(20, 8, 8)
        
        # Apply coefficient selection with attention-based importance
        selected_coeffs_list = []
        for i in range(coeffs_2d.shape[0]):
            selected, _ = attention.adaptive_coefficient_selection(
                coeffs_2d[i], 
                np.full((8, 8), importance[i]), 
                keep_ratio=0.3
            )
            selected_coeffs_list.append(selected)
        
        # Estimate entropy for each selected coefficient set
        entropy_infos = []
        for selected in selected_coeffs_list:
            info = entropy_coder.estimate_bits(selected)
            entropy_infos.append(info)
        
        # All should produce valid entropy estimates
        for info in entropy_infos:
            assert 'total_bits' in info
            assert info['total_bits'] >= 0

    def test_different_patch_sizes_compatibility(self):
        """Test that attention works with different patch sizes."""
        patch_sizes = [4, 8, 16]
        
        for patch_size in patch_sizes:
            embed_dim = patch_size * patch_size
            attention = AttentionWaveletTransform(embed_dim=embed_dim, num_heads=4, seed=42)
            
            # Create patches
            num_patches = 10
            patches = np.random.randn(num_patches, embed_dim) * 50 + 128
            
            # Apply attention
            attended, importance = attention.multi_head_attention(patches)
            
            # Should work for all patch sizes
            assert attended.shape == patches.shape
            assert importance.shape == (num_patches,)
            
            # Test with 2D transforms
            for i in range(num_patches):
                patch_2d = patches[i].reshape(patch_size, patch_size)
                coeffs = attention.wavelet_transform_2d(patch_2d)
                reconstructed = attention.inverse_wavelet_transform_2d(coeffs)
                
                np.testing.assert_allclose(reconstructed, patch_2d, atol=1e-10)

    def test_extreme_values_handling(self):
        """Test handling of extreme coefficient values."""
        attention = AttentionWaveletTransform(embed_dim=64, num_heads=4, seed=42)
        entropy_coder = AdaptiveNeuralEntropyCoder(seed=42)
        
        # Test with extreme values
        extreme_patches = np.array([
            np.full(64, 0),      # All zeros
            np.full(64, 255),    # All max values
            np.full(64, -255),   # All negative max
            np.concatenate([np.full(32, -255), np.full(32, 255)])  # Sharp transition
        ])
        
        # Should handle without errors
        attended, importance = attention.multi_head_attention(extreme_patches)
        assert attended.shape == extreme_patches.shape
        assert importance.shape == (4,)
        
        # Entropy estimation should also work
        for i in range(extreme_patches.shape[0]):
            patch_2d = extreme_patches[i].reshape(8, 8)
            info = entropy_coder.estimate_bits(patch_2d)
            assert 'total_bits' in info