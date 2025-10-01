"""Tests for the multi-scale attention functionality."""

import numpy as np
import pytest
from hqitc import HQITCCompressor
from hqitc.multiscale import MultiScaleAttentionTransform


# Global fixtures for all test classes
@pytest.fixture
def test_image_64():
    """Create a 64x64 test image for multi-scale testing."""
    size = 64
    # Create image with different frequency content at different scales
    x, y = np.meshgrid(range(size), range(size))
    
    # Combine multiple patterns
    fine_pattern = np.sin(x * 0.5) * np.cos(y * 0.5) * 50
    medium_pattern = np.sin(x * 0.1) * np.cos(y * 0.1) * 100
    coarse_pattern = ((x // 16) % 2) ^ ((y // 16) % 2)
    
    image = 128 + fine_pattern + medium_pattern + coarse_pattern * 50
    return np.clip(image, 0, 255).astype(np.float32)


class TestMultiScaleAttentionTransform:
    """Test multi-scale attention mechanism."""

    @pytest.fixture
    def multiscale_transform(self):
        """Create a MultiScaleAttentionTransform instance."""
        return MultiScaleAttentionTransform(scales=[4, 8, 16], embed_dim=64, seed=42)

    def test_initialization(self, multiscale_transform):
        """Test MultiScaleAttentionTransform initialization."""
        assert multiscale_transform.scales == [4, 8, 16]
        assert len(multiscale_transform.scale_attention) == 3
        
        # Check that each scale has appropriate attention mechanism
        for scale in [4, 8, 16]:
            assert scale in multiscale_transform.scale_attention
            # Each scale should have attention mechanism with correct dimensions
            attention = multiscale_transform.scale_attention[scale]
            expected_dim = scale * scale
            assert attention.embed_dim == expected_dim

    def test_extract_multiscale_patches(self, multiscale_transform, test_image_64):
        """Test multi-scale patch extraction."""
        patches_dict = multiscale_transform.extract_multiscale_patches(test_image_64)
        
        # Should extract patches at all scales
        assert len(patches_dict) == 3
        
        expected_patch_counts = {
            4: (64 // 4) ** 2,   # 16x16 = 256 patches  
            8: (64 // 8) ** 2,   # 8x8 = 64 patches
            16: (64 // 16) ** 2  # 4x4 = 16 patches
        }
        
        for scale, (patches, positions) in patches_dict.items():
            expected_count = expected_patch_counts[scale]
            assert patches.shape[0] == expected_count
            assert patches.shape[1] == scale * scale  # Flattened patch dimension
            assert len(positions) == expected_count

    def test_hierarchical_attention(self, multiscale_transform, test_image_64):
        """Test hierarchical attention computation."""
        patches_dict = multiscale_transform.extract_multiscale_patches(test_image_64)
        attention_results = multiscale_transform.hierarchical_attention(patches_dict)
        
        # Should have attention results for all scales
        assert len(attention_results) == 3
        
        for scale in [4, 8, 16]:
            assert scale in attention_results
            attended_patches, importance = attention_results[scale]
            
            # Check shapes
            original_patches = patches_dict[scale][0]
            assert attended_patches.shape == original_patches.shape
            assert importance.shape[0] == original_patches.shape[0]
            
            # Importance scores should be valid
            assert np.all(importance >= 0)
            assert np.all(importance <= 1)

    def test_adaptive_coefficient_selection_multiscale(self, multiscale_transform):
        """Test multi-scale coefficient selection."""
        # Create mock attention results and patches
        mock_results = {}
        mock_patches = {}
        scales = [4, 8, 16]
        
        for scale in scales:
            num_patches = 16 if scale == 16 else 64 if scale == 8 else 256
            patch_dim = scale * scale
            
            # Create some variation in coefficients and patches
            attended_patches = np.random.randn(num_patches, patch_dim) * 50
            importance = np.random.rand(num_patches) * 0.5 + 0.5
            patches = np.random.randn(num_patches, patch_dim) * 50 + 128
            positions = [(i, j) for i in range(int(np.sqrt(num_patches))) for j in range(int(np.sqrt(num_patches)))]
            
            mock_results[scale] = (attended_patches, importance)
            mock_patches[scale] = (patches, positions)
        
        # Test coefficient selection
        selected_coeffs = multiscale_transform.adaptive_coefficient_selection_multiscale(
            mock_results, mock_patches, keep_ratio=0.3
        )
        
        # Should return results for all scales
        assert len(selected_coeffs) == len(scales)
        
        for scale in scales:
            assert scale in selected_coeffs
            
            original_shape = mock_results[scale][0].shape
            assert selected_coeffs[scale].shape == original_shape

    def test_scale_fusion(self, multiscale_transform):
        """Test cross-scale fusion mechanism."""
        # Create mock features at different scales
        small_features = np.random.randn(16, 16)  # 4x4 patches -> 16 dims
        large_features = np.random.randn(64, 64)  # 8x8 patches -> 64 dims
        
        # Test fusion (this tests internal _fuse_scales method indirectly)
        # The fusion should handle dimension mismatches gracefully
        fused = multiscale_transform._fuse_scales(large_features, small_features, 8)
        
        # Output should match current features shape
        assert fused.shape == large_features.shape


@pytest.fixture
def multiscale_compressor():
    """Create compressor with multi-scale attention."""
    return HQITCCompressor(
        use_multiscale=True,
        multiscale_sizes=[4, 8, 16],
        use_quantum=False
    )

@pytest.fixture
def singlescale_compressor():
    """Create standard single-scale compressor for comparison."""
    return HQITCCompressor(use_multiscale=False, use_quantum=False)


class TestMultiScaleCompression:
    """Test multi-scale compression functionality."""

    def test_multiscale_compression_structure(self, multiscale_compressor, test_image_64):
        """Test multi-scale compression output structure."""
        compressed = multiscale_compressor.compress(test_image_64, verbose=False)
        
        # Should have multi-scale specific structure
        assert compressed['type'] == 'multiscale'
        assert 'quantized_scales' in compressed
        assert 'entropy_info_scales' in compressed
        assert 'scales' in compressed
        
        # Should have data for all scales
        expected_scales = [4, 8, 16]
        for scale in expected_scales:
            assert scale in compressed['quantized_scales']
            assert scale in compressed['entropy_info_scales']

    def test_multiscale_decompression(self, multiscale_compressor, test_image_64):
        """Test multi-scale decompression."""
        compressed = multiscale_compressor.compress(test_image_64, verbose=False)
        reconstructed = multiscale_compressor.decompress(compressed, verbose=False)
        
        # Basic shape preservation
        assert reconstructed.shape == test_image_64.shape
        
        # Should achieve reasonable quality
        mse = np.mean((test_image_64 - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        assert psnr > 10  # Should achieve at least 10 dB

    def test_multiscale_vs_singlescale_comparison(self, multiscale_compressor, 
                                                 singlescale_compressor, test_image_64):
        """Compare multi-scale vs single-scale performance."""
        # Compress with both methods
        multi_compressed = multiscale_compressor.compress(test_image_64, verbose=False)
        single_compressed = singlescale_compressor.compress(test_image_64, verbose=False)
        
        # Decompress both 
        multi_reconstructed = multiscale_compressor.decompress(multi_compressed, verbose=False)
        single_reconstructed = singlescale_compressor.decompress(single_compressed, verbose=False)
        
        # Both should preserve shape
        assert multi_reconstructed.shape == test_image_64.shape
        assert single_reconstructed.shape == test_image_64.shape
        
        # Calculate quality metrics
        multi_mse = np.mean((test_image_64 - multi_reconstructed) ** 2)
        single_mse = np.mean((test_image_64 - single_reconstructed) ** 2)
        
        multi_psnr = 10 * np.log10((255.0 ** 2) / (multi_mse + 1e-12))
        single_psnr = 10 * np.log10((255.0 ** 2) / (single_mse + 1e-12))
        
        # Both should achieve reasonable quality
        assert multi_psnr > 10
        assert single_psnr > 10
        
        # Methods may have different trade-offs, but both should work
        assert multi_compressed['compression_ratio'] > 1
        assert single_compressed['compression_ratio'] > 1

    @pytest.mark.parametrize("scales", [
        [4, 8],
        [8, 16], 
        [4, 8, 16],
        [4, 8, 16, 32]
    ])
    def test_different_scale_combinations(self, scales, test_image_64):
        """Test different combinations of scales."""
        # Skip if image too small for largest scale
        max_scale = max(scales)
        if test_image_64.shape[0] < max_scale or test_image_64.shape[1] < max_scale:
            pytest.skip(f"Image too small for scale {max_scale}")
        
        compressor = HQITCCompressor(
            use_multiscale=True,
            multiscale_sizes=scales,
            use_quantum=False
        )
        
        compressed = compressor.compress(test_image_64, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        # Should work with any valid scale combination
        assert reconstructed.shape == test_image_64.shape
        
        # Should have data for all requested scales
        for scale in scales:
            if scale <= min(test_image_64.shape):  # Only if scale fits in image
                assert scale in compressed['quantized_scales']

    def test_multiscale_quality_factors(self, multiscale_compressor, test_image_64):
        """Test multi-scale compression with different quality factors."""
        quality_factors = [0.3, 0.6, 0.9]
        results = {}
        
        for quality in quality_factors:
            compressed = multiscale_compressor.compress(
                test_image_64, 
                quality_factor=quality, 
                verbose=False
            )
            reconstructed = multiscale_compressor.decompress(compressed, verbose=False)
            
            mse = np.mean((test_image_64 - reconstructed) ** 2)
            psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
            
            results[quality] = {
                'psnr': psnr,
                'compression_ratio': compressed['compression_ratio']
            }
        
        # Higher quality should generally mean better PSNR
        assert results[0.9]['psnr'] >= results[0.6]['psnr'] - 5  # Allow some tolerance
        
        # All should achieve reasonable compression
        for quality in quality_factors:
            assert results[quality]['compression_ratio'] > 1


class TestMultiScaleEdgeCases:
    """Test edge cases for multi-scale processing."""

    def test_image_too_small_for_largest_scale(self):
        """Test handling when image is too small for largest scale."""
        compressor = HQITCCompressor(
            use_multiscale=True,
            multiscale_sizes=[4, 8, 32],  # 32 is too large for small image
            use_quantum=False
        )
        
        small_image = np.random.rand(16, 16) * 255  # Only 16x16
        
        # Should handle gracefully (skip scales that don't fit)
        compressed = compressor.compress(small_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == small_image.shape

    def test_single_scale_multiscale_mode(self):
        """Test multi-scale mode with only one scale."""
        compressor = HQITCCompressor(
            use_multiscale=True,
            multiscale_sizes=[8],  # Only one scale
            use_quantum=False
        )
        
        test_image = np.random.rand(32, 32) * 255
        
        compressed = compressor.compress(test_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == test_image.shape

    def test_multiscale_with_uniform_image(self, multiscale_compressor):
        """Test multi-scale processing with uniform image."""
        uniform_image = np.full((64, 64), 128, dtype=np.float32)
        
        compressed = multiscale_compressor.compress(uniform_image, verbose=False)
        reconstructed = multiscale_compressor.decompress(compressed, verbose=False)
        
        # Should achieve very high quality for uniform content
        mse = np.mean((uniform_image - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        assert psnr > 30

    def test_multiscale_memory_efficiency(self, multiscale_compressor):
        """Test that multi-scale doesn't use excessive memory."""
        # Create larger image to test memory usage
        large_image = np.random.rand(128, 128) * 255
        
        # This should complete without memory errors
        compressed = multiscale_compressor.compress(large_image, verbose=False)
        reconstructed = multiscale_compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == large_image.shape


@pytest.fixture  
def color_multiscale_compressor():
    """Create compressor with both color and multi-scale enabled."""
    return HQITCCompressor(
        use_multiscale=True,
        multiscale_sizes=[4, 8, 16],
        color_mode='auto',
        use_quantum=False
    )


class TestMultiScaleColorIntegration:
    """Test integration of multi-scale with color processing."""

    @pytest.fixture
    def color_test_image(self):
        """Create color test image for multi-scale testing."""
        size = 64
        image = np.zeros((size, size, 3))
        
        # Different patterns in each channel
        x, y = np.meshgrid(range(size), range(size))
        image[:, :, 0] = np.sin(x * 0.2) * 127 + 128  # Red sine wave
        image[:, :, 1] = ((x // 8) % 2) ^ ((y // 8) % 2) * 255  # Green checkerboard
        image[:, :, 2] = np.linspace(0, 255, size).reshape(1, -1)  # Blue gradient
        
        return image.astype(np.float32)

    def test_color_multiscale_compression(self, color_multiscale_compressor, color_test_image):
        """Test color image compression with multi-scale attention."""
        compressed = color_multiscale_compressor.compress(color_test_image, verbose=False)
        
        # Should have color structure
        assert compressed['type'] == 'color'
        assert 'channels' in compressed  # Actual key is 'channels', not 'compressed_channels'
        
        # Each channel should be compressed with multi-scale
        for channel_data in compressed['channels'].values():
            assert channel_data['type'] == 'multiscale'

    def test_color_multiscale_decompression(self, color_multiscale_compressor, color_test_image):
        """Test color multi-scale decompression."""
        compressed = color_multiscale_compressor.compress(color_test_image, verbose=False)
        reconstructed = color_multiscale_compressor.decompress(compressed, verbose=False)
        
        # Should preserve color image properties
        assert reconstructed.shape == color_test_image.shape
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 255)
        
        # Should achieve reasonable quality
        mse = np.mean((color_test_image - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        assert psnr > 10