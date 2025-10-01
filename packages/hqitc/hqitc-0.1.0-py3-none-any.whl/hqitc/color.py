"""
Color space utilities for HQITC compression.
Handles RGB to YUV conversion and channel-specific processing.
"""

import numpy as np
from typing import Tuple, Dict, Any


class ColorSpaceProcessor:
    """Handles color space conversions and channel-specific compression settings."""
    
    def __init__(self):
        # ITU-R BT.601 YUV conversion matrix
        self.rgb_to_yuv_matrix = np.array([
            [0.299, 0.587, 0.114],      # Y
            [-0.14713, -0.28886, 0.436],  # U  
            [0.615, -0.51499, -0.10001]   # V
        ])
        
        self.yuv_to_rgb_matrix = np.linalg.inv(self.rgb_to_yuv_matrix)
        
        # Channel-specific compression settings
        self.channel_settings = {
            'Y': {'quality_weight': 1.0, 'keep_ratio_multiplier': 1.0},  # Luminance - high quality
            'U': {'quality_weight': 0.7, 'keep_ratio_multiplier': 0.6},  # Chrominance - reduced quality
            'V': {'quality_weight': 0.7, 'keep_ratio_multiplier': 0.6}   # Chrominance - reduced quality
        }
    
    def rgb_to_yuv(self, rgb_image: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Convert RGB image to YUV color space.
        
        Args:
            rgb_image: RGB image array of shape (H, W, 3) with values in [0, 255]
            
        Returns:
            Dictionary with 'Y', 'U', 'V' channel arrays
        """
        if rgb_image.ndim != 3 or rgb_image.shape[2] != 3:
            raise ValueError("RGB image must have shape (H, W, 3)")
        
        # Normalize to [0, 1] range
        rgb_normalized = rgb_image / 255.0
        
        # Reshape for matrix multiplication
        h, w, c = rgb_image.shape
        rgb_flat = rgb_normalized.reshape(-1, 3)
        
        # Apply conversion matrix
        yuv_flat = rgb_flat @ self.rgb_to_yuv_matrix.T
        
        # Reshape back and convert to [0, 255] range
        yuv = yuv_flat.reshape(h, w, 3)
        
        # Scale channels appropriately
        yuv_scaled = np.zeros_like(yuv)
        yuv_scaled[:, :, 0] = yuv[:, :, 0] * 255.0  # Y: [0, 255]
        yuv_scaled[:, :, 1] = (yuv[:, :, 1] + 0.436) * 255.0 / (2 * 0.436)  # U: [-0.436, 0.436] -> [0, 255]
        yuv_scaled[:, :, 2] = (yuv[:, :, 2] + 0.615) * 255.0 / (2 * 0.615)  # V: [-0.615, 0.615] -> [0, 255]
        
        return {
            'Y': np.clip(yuv_scaled[:, :, 0], 0, 255).astype(np.float32),
            'U': np.clip(yuv_scaled[:, :, 1], 0, 255).astype(np.float32),
            'V': np.clip(yuv_scaled[:, :, 2], 0, 255).astype(np.float32)
        }
    
    def yuv_to_rgb(self, yuv_channels: Dict[str, np.ndarray]) -> np.ndarray:
        """
        Convert YUV channels back to RGB image.
        
        Args:
            yuv_channels: Dictionary with 'Y', 'U', 'V' channel arrays
            
        Returns:
            RGB image array of shape (H, W, 3)
        """
        Y, U, V = yuv_channels['Y'], yuv_channels['U'], yuv_channels['V']
        h, w = Y.shape
        
        # Convert back to YUV ranges
        yuv_array = np.zeros((h, w, 3))
        yuv_array[:, :, 0] = Y / 255.0  # Y: [0, 1]
        yuv_array[:, :, 1] = (U / 255.0) * (2 * 0.436) - 0.436  # U: [0, 1] -> [-0.436, 0.436]
        yuv_array[:, :, 2] = (V / 255.0) * (2 * 0.615) - 0.615  # V: [0, 1] -> [-0.615, 0.615]
        
        # Reshape for matrix multiplication
        yuv_flat = yuv_array.reshape(-1, 3)
        
        # Apply inverse conversion matrix
        rgb_flat = yuv_flat @ self.yuv_to_rgb_matrix.T
        
        # Reshape back and convert to [0, 255] range
        rgb_image = rgb_flat.reshape(h, w, 3) * 255.0
        
        return np.clip(rgb_image, 0, 255).astype(np.uint8)
    
    def get_channel_compression_params(self, channel: str, base_quality: float, base_keep_ratio: float) -> Tuple[float, float]:
        """
        Get channel-specific compression parameters.
        
        Args:
            channel: Channel name ('Y', 'U', or 'V')
            base_quality: Base quality factor
            base_keep_ratio: Base coefficient keep ratio
            
        Returns:
            Tuple of (adjusted_quality, adjusted_keep_ratio)
        """
        settings = self.channel_settings.get(channel, self.channel_settings['Y'])
        
        adjusted_quality = base_quality * settings['quality_weight']
        adjusted_keep_ratio = base_keep_ratio * settings['keep_ratio_multiplier']
        
        return adjusted_quality, adjusted_keep_ratio
    
    def compute_color_importance_weights(self, yuv_channels: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Compute importance weights for each channel based on content.
        
        Args:
            yuv_channels: YUV channel dictionary
            
        Returns:
            Dictionary of importance weight arrays for each channel
        """
        weights = {}
        
        for channel, image in yuv_channels.items():
            # Compute local variance as importance measure
            # Use 3x3 kernel for local variance computation
            padded = np.pad(image, 1, mode='reflect')
            variance_map = np.zeros_like(image)
            
            for i in range(1, padded.shape[0] - 1):
                for j in range(1, padded.shape[1] - 1):
                    local_patch = padded[i-1:i+2, j-1:j+2]
                    variance_map[i-1, j-1] = np.var(local_patch)
            
            # Normalize to [0, 1] range
            if variance_map.max() > 0:
                variance_map = variance_map / variance_map.max()
            
            # Apply channel-specific weighting
            channel_weight = self.channel_settings[channel]['quality_weight']
            weights[channel] = 0.3 + 0.7 * variance_map * channel_weight
        
        return weights