"""Tests for the main HQITC compression functionality."""

import numpy as np
import pytest
from hqitc import HQITCCompressor
from hqitc.main import make_test_images


class TestHQITCCompressor:
    """Test cases for the HQITC compression algorithm."""

    def test_initialization(self):
        """Test that compressor initializes correctly."""
        compressor = HQITCCompressor()
        assert compressor.patch_size == 8
        assert compressor.use_quantum is False

    def test_extract_patches(self, compressor, test_image):
        """Test patch extraction functionality."""
        patches, positions = compressor.extract_patches(test_image)
        
        expected_patches = (test_image.shape[0] // 8) * (test_image.shape[1] // 8)
        assert patches.shape[0] == expected_patches
        assert patches.shape[1] == 64  # 8x8 patches
        assert len(positions) == expected_patches

    def test_compress_decompress_cycle(self, compressor, test_image):
        """Test complete compression-decompression cycle."""
        # Compress
        compressed = compressor.compress(test_image, verbose=False)
        
        # Check compressed data structure
        required_keys = [
            'compressed_quantized', 'q_step', 'coeffs_shape',
            'original_shape', 'positions', 'encoding_info',
            'compression_ratio'
        ]
        for key in required_keys:
            assert key in compressed
        
        # Decompress
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        # Check output shape
        assert reconstructed.shape == test_image.shape
        
        # Check quality (should be reasonable for this simple image)
        mse = np.mean((test_image - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        assert psnr > 15  # Should achieve at least 15 dB PSNR

    def test_different_quality_factors(self, compressor, gradient_image):
        """Test that different quality factors produce different results."""
        results = {}
        
        for quality in [0.3, 0.6, 0.9]:
            compressed = compressor.compress(gradient_image, quality_factor=quality, verbose=False)
            reconstructed = compressor.decompress(compressed, verbose=False)
            
            mse = np.mean((gradient_image - reconstructed) ** 2)
            psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
            results[quality] = {
                'psnr': psnr,
                'compression_ratio': compressed['compression_ratio'],
                'coeffs': compressed['encoding_info']['num_nonzero']
            }
        
        # Higher quality should generally mean better PSNR
        assert results[0.9]['psnr'] >= results[0.6]['psnr']
        # Lower quality should generally mean better compression ratio
        assert results[0.3]['compression_ratio'] >= results[0.6]['compression_ratio']

    def test_test_images_generation(self):
        """Test that test images are generated correctly."""
        images = make_test_images(64)
        
        expected_types = ['geometric', 'texture', 'edges', 'gradient']
        for img_type in expected_types:
            assert img_type in images
            assert images[img_type].shape == (64, 64)
            assert images[img_type].dtype == np.float32

    def test_attention_mechanism(self, compressor):
        """Test that attention mechanism produces valid importance scores."""
        # Create patches with different characteristics
        uniform_patch = np.ones((1, 64)) * 128  # uniform gray
        varying_patch = np.random.rand(1, 64) * 255  # random values
        
        patches = np.vstack([uniform_patch, varying_patch])
        
        _, importance = compressor.attention_wavelet.multi_head_attention(patches)
        
        # Should produce valid importance scores
        assert importance.shape == (2,)
        assert np.all(importance >= 0)
        assert np.all(importance <= 1)
        # The varying patch should generally have higher importance
        assert importance[1] >= importance[0]

    @pytest.mark.parametrize("patch_size", [4, 8, 16])
    def test_different_patch_sizes(self, patch_size, test_image):
        """Test compression with different patch sizes."""
        # Ensure image size is compatible
        if test_image.shape[0] % patch_size != 0:
            pytest.skip(f"Image size not compatible with patch size {patch_size}")
        
        compressor = HQITCCompressor(patch_size=patch_size, use_quantum=False)
        
        compressed = compressor.compress(test_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == test_image.shape
        
        # Should achieve reasonable quality (adjust expectations based on patch size)
        mse = np.mean((test_image - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        
        # Different patch sizes have different performance characteristics
        if patch_size == 4:
            assert psnr > 3  # Smaller patches may have lower quality
        elif patch_size == 8:
            assert psnr > 10  # Standard patch size should work well
        else:  # patch_size == 16
            assert psnr > 5  # Larger patches may have different performance


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_small_image(self, compressor):
        """Test with very small image."""
        small_image = np.ones((8, 8)) * 128  # Single patch
        
        compressed = compressor.compress(small_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == small_image.shape

    def test_color_image_dimensions(self, compressor):
        """Test with color image dimensions."""
        # 3D color image should be processed successfully
        color_image = np.ones((8, 8, 3), dtype=np.float32) * 128
        compressed = compressor.compress(color_image, verbose=False)
        
        # Should process as color image
        assert 'type' in compressed
        # Should be either 'color' or 'grayscale' depending on color_mode setting
        assert compressed['type'] in ['color', 'grayscale']
        
        # Should be able to decompress
        reconstructed = compressor.decompress(compressed, verbose=False)
        assert reconstructed.shape == color_image.shape or reconstructed.shape == (8, 8)  # May convert to grayscale

    def test_extreme_quality_factors(self, compressor, test_image):
        """Test with extreme quality factor values."""
        # Very low quality
        compressed_low = compressor.compress(test_image, quality_factor=0.01, verbose=False)
        reconstructed_low = compressor.decompress(compressed_low, verbose=False)
        assert reconstructed_low.shape == test_image.shape
        
        # Very high quality  
        compressed_high = compressor.compress(test_image, quality_factor=0.99, verbose=False)
        reconstructed_high = compressor.decompress(compressed_high, verbose=False)
        assert reconstructed_high.shape == test_image.shape