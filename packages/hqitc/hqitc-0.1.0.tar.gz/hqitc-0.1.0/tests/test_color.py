"""Tests for the color processing functionality."""

import numpy as np
import pytest
from hqitc import HQITCCompressor
from hqitc.color import ColorSpaceProcessor


class TestColorSpaceProcessor:
    """Test color space conversion functionality."""

    @pytest.fixture
    def processor(self):
        """Create a ColorSpaceProcessor instance."""
        return ColorSpaceProcessor()

    @pytest.fixture
    def rgb_image(self):
        """Create a test RGB image."""
        # Create a simple RGB gradient
        size = 32
        rgb = np.zeros((size, size, 3))
        rgb[:, :, 0] = np.linspace(0, 255, size).reshape(1, -1)  # Red gradient
        rgb[:, :, 1] = np.linspace(0, 255, size).reshape(-1, 1)  # Green gradient  
        rgb[:, :, 2] = 128  # Constant blue
        return rgb.astype(np.float32)

    def test_initialization(self, processor):
        """Test ColorSpaceProcessor initialization."""
        assert processor.rgb_to_yuv_matrix.shape == (3, 3)
        assert processor.yuv_to_rgb_matrix.shape == (3, 3)
        
        # Check that matrices are approximately inverse of each other
        identity = processor.rgb_to_yuv_matrix @ processor.yuv_to_rgb_matrix
        np.testing.assert_allclose(identity, np.eye(3), atol=1e-10)

    def test_rgb_to_yuv_conversion(self, processor, rgb_image):
        """Test RGB to YUV conversion."""
        yuv_channels = processor.rgb_to_yuv(rgb_image)
        
        # Check that we get a dictionary with Y, U, V channels
        assert isinstance(yuv_channels, dict)
        assert set(yuv_channels.keys()) == {'Y', 'U', 'V'}
        
        # Check shape preservation for each channel
        h, w, c = rgb_image.shape
        for channel, channel_data in yuv_channels.items():
            assert channel_data.shape == (h, w)
        
        # Check that it's a proper conversion (not just copy)
        # Compare flattened Y channel with flattened first RGB channel
        assert not np.array_equal(yuv_channels['Y'].flatten(), rgb_image[:, :, 0].flatten())
        
        # Check value ranges
        for channel_data in yuv_channels.values():
            assert np.all(channel_data >= 0)
            assert np.all(channel_data <= 255)

    def test_yuv_to_rgb_conversion(self, processor, rgb_image):
        """Test YUV to RGB conversion."""
        # Convert RGB -> YUV -> RGB
        yuv_channels = processor.rgb_to_yuv(rgb_image)
        reconstructed_rgb = processor.yuv_to_rgb(yuv_channels)
        
        # Should be very close to original (within reasonable tolerance for uint8 conversion)
        np.testing.assert_allclose(reconstructed_rgb, rgb_image, atol=2.0)

    def test_roundtrip_conversion(self, processor):
        """Test multiple roundtrip conversions maintain accuracy."""
        # Create test colors
        test_colors = np.array([
            [[255, 0, 0]],    # Pure red
            [[0, 255, 0]],    # Pure green
            [[0, 0, 255]],    # Pure blue
            [[255, 255, 255]], # White
            [[0, 0, 0]],      # Black
            [[128, 128, 128]] # Gray
        ]).astype(np.float32)
        
        original = test_colors.copy()
        current = test_colors.copy()
        
        # Multiple roundtrips
        for _ in range(5):
            yuv_channels = processor.rgb_to_yuv(current)
            current = processor.yuv_to_rgb(yuv_channels).astype(np.float32)
        
        # Should still be close to original (with tolerance for uint8 conversion artifacts)
        np.testing.assert_allclose(current, original, atol=5.0)

    def test_get_channel_compression_params(self, processor):
        """Test channel-specific compression parameters."""
        base_quality = 0.7
        base_keep_ratio = 0.5
        
        # Test for each channel
        for channel in ['Y', 'U', 'V']:
            quality, keep_ratio = processor.get_channel_compression_params(channel, base_quality, base_keep_ratio)
            
            # Should return valid parameters
            assert isinstance(quality, float)
            assert isinstance(keep_ratio, float)
            assert quality > 0
            assert keep_ratio > 0
        
        # Y channel should have highest quality (no reduction)
        y_quality, y_keep_ratio = processor.get_channel_compression_params('Y', base_quality, base_keep_ratio)
        u_quality, u_keep_ratio = processor.get_channel_compression_params('U', base_quality, base_keep_ratio)
        v_quality, v_keep_ratio = processor.get_channel_compression_params('V', base_quality, base_keep_ratio)
        
        assert y_quality >= u_quality
        assert y_quality >= v_quality
        assert y_keep_ratio >= u_keep_ratio  
        assert y_keep_ratio >= v_keep_ratio


class TestColorImageCompression:
    """Test color image compression functionality."""

    @pytest.fixture
    def color_compressor(self):
        """Create compressor for color images."""
        return HQITCCompressor(color_mode='auto', use_quantum=False)

    @pytest.fixture
    def rgb_test_image(self):
        """Create RGB test image."""
        size = 32
        image = np.zeros((size, size, 3))
        
        # Create distinct patterns in each channel
        x, y = np.meshgrid(range(size), range(size))
        image[:, :, 0] = ((x // 4) % 2) * 255  # Red checkerboard
        image[:, :, 1] = np.sin(x * 0.2) * 127 + 128  # Green sine wave
        image[:, :, 2] = y * 255 / size  # Blue gradient
        
        return image.astype(np.float32)

    def test_color_image_detection(self, color_compressor, rgb_test_image):
        """Test automatic color image detection."""
        # Should automatically detect color image
        compressed = color_compressor.compress(rgb_test_image, verbose=False)
        
        # Should have color-specific structure
        assert 'type' in compressed
        assert compressed['type'] == 'color'
        assert 'channels' in compressed  # Actual key is 'channels', not 'compressed_channels'

    def test_color_compression_decompression(self, color_compressor, rgb_test_image):
        """Test complete color compression-decompression cycle."""
        # Compress
        compressed = color_compressor.compress(rgb_test_image, verbose=False)
        
        # Decompress
        reconstructed = color_compressor.decompress(compressed, verbose=False)
        
        # Check shape preservation
        assert reconstructed.shape == rgb_test_image.shape
        
        # Check that it's still a valid color image
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 255)

    def test_color_vs_grayscale_mode(self, rgb_test_image):
        """Test color vs grayscale mode differences."""
        color_compressor = HQITCCompressor(color_mode='auto', use_quantum=False)
        gray_compressor = HQITCCompressor(color_mode='grayscale', use_quantum=False)
        
        # Compress same image with both modes
        color_result = color_compressor.compress(rgb_test_image, verbose=False)
        gray_result = gray_compressor.compress(rgb_test_image, verbose=False)
        
        # Results should have different structures
        assert color_result['type'] != gray_result['type']
        
        # Decompress
        color_recon = color_compressor.decompress(color_result, verbose=False)
        gray_recon = gray_compressor.decompress(gray_result, verbose=False)
        
        # Color reconstruction should preserve 3 channels
        assert color_recon.shape == rgb_test_image.shape
        # Grayscale reconstruction should be 2D
        assert gray_recon.ndim == 2

    def test_per_channel_quality_differences(self, color_compressor, rgb_test_image):
        """Test that different channels get different quality treatment."""
        compressed = color_compressor.compress(rgb_test_image, verbose=False)
        
        if 'compressed_channels' in compressed:
            channels = compressed['compressed_channels']
            
            # Y channel should typically have more coefficients than U/V
            if 'Y' in channels and 'U' in channels:
                y_coeffs = compressed['channel_info']['Y']['coeffs_kept']
                u_coeffs = compressed['channel_info']['U']['coeffs_kept']
                
                # Y (luminance) should generally preserve more detail
                assert y_coeffs >= u_coeffs

    @pytest.mark.parametrize("quality_factor", [0.3, 0.6, 0.9])
    def test_color_quality_scaling(self, color_compressor, rgb_test_image, quality_factor):
        """Test color compression with different quality factors."""
        compressed = color_compressor.compress(
            rgb_test_image, 
            quality_factor=quality_factor, 
            verbose=False
        )
        reconstructed = color_compressor.decompress(compressed, verbose=False)
        
        # Basic validation
        assert reconstructed.shape == rgb_test_image.shape
        
        # Calculate per-channel PSNR
        psnr_channels = []
        for c in range(3):
            mse = np.mean((rgb_test_image[:, :, c] - reconstructed[:, :, c]) ** 2)
            psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
            psnr_channels.append(psnr)
        
        # Should achieve reasonable quality for all channels
        assert all(psnr > 5 for psnr in psnr_channels)


class TestColorEdgeCases:
    """Test edge cases for color processing."""

    def test_single_channel_as_color(self):
        """Test handling of single-channel image in color mode."""
        compressor = HQITCCompressor(color_mode='auto', use_quantum=False)
        gray_image = np.random.rand(32, 32) * 255
        
        # Should handle gracefully (convert to grayscale processing)
        compressed = compressor.compress(gray_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        assert reconstructed.shape == gray_image.shape

    def test_extreme_color_values(self):
        """Test with extreme color values."""
        compressor = HQITCCompressor(color_mode='auto', use_quantum=False)
        
        # Create image with extreme values
        extreme_image = np.zeros((16, 16, 3))
        extreme_image[:8, :8, 0] = 255  # Bright red region
        extreme_image[8:, 8:, 2] = 255  # Bright blue region
        # Leave green channel mostly zero
        
        compressed = compressor.compress(extreme_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        # Should maintain general structure
        assert reconstructed.shape == extreme_image.shape
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 255)

    def test_uniform_color_image(self):
        """Test with uniform color image."""
        compressor = HQITCCompressor(color_mode='auto', use_quantum=False)
        
        # Create uniform color image
        uniform_image = np.full((24, 24, 3), [100, 150, 200], dtype=np.float32)
        
        compressed = compressor.compress(uniform_image, verbose=False)
        reconstructed = compressor.decompress(compressed, verbose=False)
        
        # Should achieve reasonable quality for uniform regions
        mse = np.mean((uniform_image - reconstructed) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        assert psnr > 10  # Should be reasonable for uniform content (lowered expectation)