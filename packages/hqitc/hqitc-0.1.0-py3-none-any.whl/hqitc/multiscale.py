"""
Multi-scale attention mechanism for HQITC.
Processes patches at multiple scales to capture both local and global features.
"""

import numpy as np
from scipy.fft import dct, idct
from typing import Tuple, Dict, List
from .utils import AttentionWaveletTransform


class MultiScaleAttentionTransform:
    """
    Multi-scale attention mechanism that processes patches at different scales.
    Hierarchical processing: 4x4 -> 8x8 -> 16x16
    """
    
    def __init__(self, scales: List[int] = [4, 8, 16], embed_dim: int = 64, seed: int = 42):
        """
        Initialize multi-scale attention transform.
        
        Args:
            scales: List of patch sizes to process (e.g., [4, 8, 16])
            embed_dim: Embedding dimension for attention
            seed: Random seed for reproducibility
        """
        self.scales = sorted(scales)  # Process from smallest to largest
        self.embed_dim = embed_dim
        self.seed = seed
        
        # Create attention mechanism for each scale
        # Each scale needs its own embedding dimension based on patch size
        self.scale_attention = {}
        for scale in scales:
            patch_dim = scale * scale  # 4x4=16, 8x8=64, 16x16=256
            self.scale_attention[scale] = AttentionWaveletTransform(patch_dim, num_heads=8, seed=seed)
        
        # Cross-scale fusion weights
        np.random.seed(seed)
        self.fusion_weights = {}
        for i, scale in enumerate(scales[1:], 1):  # Skip first scale
            prev_scale = scales[i-1]
            current_patch_dim = scale * scale
            prev_patch_dim = prev_scale * prev_scale
            # Weights for combining current scale with previous scales
            self.fusion_weights[scale] = {
                'self_weight': 0.7,
                'prev_weight': 0.3,
                'adaptation': np.random.randn(current_patch_dim, current_patch_dim) * 0.1
            }
    
    def extract_multiscale_patches(self, image: np.ndarray) -> Dict[int, Tuple[np.ndarray, List]]:
        """
        Extract patches at multiple scales from the image.
        
        Args:
            image: Input image (H, W)
            
        Returns:
            Dictionary mapping scale -> (patches, positions)
        """
        h, w = image.shape
        multiscale_patches = {}
        
        for scale in self.scales:
            if h >= scale and w >= scale:
                patches = []
                positions = []
                
                # Extract non-overlapping patches
                for i in range(0, h - scale + 1, scale):
                    for j in range(0, w - scale + 1, scale):
                        patch = image[i:i+scale, j:j+scale]
                        patches.append(patch.flatten())
                        positions.append((i, j))
                
                multiscale_patches[scale] = (np.array(patches), positions)
            else:
                print(f"Warning: Image too small for scale {scale}x{scale}")
        
        return multiscale_patches
    
    def hierarchical_attention(self, multiscale_patches: Dict[int, Tuple[np.ndarray, List]]) -> Dict[int, Tuple[np.ndarray, np.ndarray]]:
        """
        Apply hierarchical attention across scales.
        
        Args:
            multiscale_patches: Dictionary of patches at different scales
            
        Returns:
            Dictionary mapping scale -> (attended_patches, importance_scores)
        """
        scale_results = {}
        prev_context = None
        
        for scale in self.scales:
            if scale not in multiscale_patches:
                continue
                
            patches, positions = multiscale_patches[scale]
            
            # Apply attention at current scale
            attended, importance = self.scale_attention[scale].multi_head_attention(patches.astype(float))
            
            # Fuse with previous scale context if available
            if prev_context is not None and scale in self.fusion_weights:
                attended = self._fuse_scales(attended, prev_context, scale)
            
            scale_results[scale] = (attended, importance)
            
            # Prepare context for next scale (downsample if needed)
            prev_context = self._prepare_context_for_next_scale(attended, importance, scale)
        
        return scale_results
    
    def _fuse_scales(self, current_features: np.ndarray, prev_context: np.ndarray, scale: int) -> np.ndarray:
        """
        Fuse features from current scale with context from previous scales.
        
        Args:
            current_features: Features at current scale
            prev_context: Context from previous scales
            scale: Current scale size
            
        Returns:
            Fused features
        """
        fusion_params = self.fusion_weights[scale]
        self_weight = fusion_params['self_weight']
        prev_weight = fusion_params['prev_weight']
        adaptation_matrix = fusion_params['adaptation']
        
        # Ensure dimensions match
        if prev_context.shape[1] != current_features.shape[1]:
            # Simple adaptation - could be more sophisticated
            if prev_context.shape[1] < current_features.shape[1]:
                padding = np.zeros((prev_context.shape[0], current_features.shape[1] - prev_context.shape[1]))
                prev_context = np.concatenate([prev_context, padding], axis=1)
            else:
                prev_context = prev_context[:, :current_features.shape[1]]
        
        # Match number of patches (simple repetition/sampling)
        if prev_context.shape[0] != current_features.shape[0]:
            if prev_context.shape[0] < current_features.shape[0]:
                # Repeat previous context
                repeat_factor = current_features.shape[0] // prev_context.shape[0] + 1
                prev_context = np.tile(prev_context, (repeat_factor, 1))[:current_features.shape[0]]
            else:
                # Sample from previous context
                indices = np.linspace(0, prev_context.shape[0]-1, current_features.shape[0], dtype=int)
                prev_context = prev_context[indices]
        
        # Apply adaptive fusion
        adapted_prev = prev_context @ adaptation_matrix
        fused = self_weight * current_features + prev_weight * adapted_prev
        
        return fused
    
    def _prepare_context_for_next_scale(self, features: np.ndarray, importance: np.ndarray, current_scale: int) -> np.ndarray:
        """
        Prepare context information for the next scale.
        
        Args:
            features: Features at current scale
            importance: Importance scores at current scale
            current_scale: Current scale size
            
        Returns:
            Context features for next scale
        """
        # Weight features by importance and aggregate
        weighted_features = features * importance.reshape(-1, 1)
        
        # Compute global context (could be more sophisticated)
        global_context = np.mean(weighted_features, axis=0, keepdims=True)
        
        # Create context that captures important patterns
        # For now, use a simple approach - could use more advanced pooling
        top_indices = np.argsort(importance)[-min(10, len(importance)):]  # Top 10 patches
        important_features = features[top_indices]
        
        # Combine global and local important context
        context = np.vstack([global_context, important_features])
        
        return context
    
    def adaptive_coefficient_selection_multiscale(self, 
                                                multiscale_results: Dict[int, Tuple[np.ndarray, np.ndarray]],
                                                multiscale_patches: Dict[int, Tuple[np.ndarray, List]],
                                                keep_ratio: float = 0.3) -> Dict[int, np.ndarray]:
        """
        Select DCT coefficients adaptively across multiple scales.
        
        Args:
            multiscale_results: Results from hierarchical attention
            multiscale_patches: Original patch data
            keep_ratio: Base coefficient keep ratio
            
        Returns:
            Dictionary of compressed coefficients for each scale
        """
        scale_coefficients = {}
        
        for scale in self.scales:
            if scale not in multiscale_results:
                continue
                
            attended_patches, importance = multiscale_results[scale]
            patches, positions = multiscale_patches[scale]
            
            # Apply DCT to each patch
            patch_coeffs = []
            expected_patch_dim = scale * scale
            
            for i, patch in enumerate(attended_patches):
                # Handle dimension mismatch
                if patch.size >= expected_patch_dim:
                    patch_data = patch[:expected_patch_dim]
                else:
                    patch_data = np.zeros(expected_patch_dim)
                    patch_data[:patch.size] = patch
                
                # Reshape and apply DCT
                patch_2d = patch_data.reshape(scale, scale)
                patch_dct = dct(dct(patch_2d, axis=0, norm='ortho'), axis=1, norm='ortho')
                patch_coeffs.append(patch_dct.flatten())
            
            patch_coeffs = np.array(patch_coeffs)
            
            # Scale-adaptive coefficient selection
            # Smaller scales get higher keep ratios (more detail preservation)
            scale_factor = min(self.scales) / scale  # Higher for smaller scales
            adjusted_keep_ratio = keep_ratio * (0.8 + 0.4 * scale_factor)
            adjusted_keep_ratio = np.clip(adjusted_keep_ratio, 0.01, 0.95)
            
            # Select coefficients based on importance
            compressed_coeffs = np.zeros_like(patch_coeffs)
            
            for i, (coeffs_patch, patch_importance) in enumerate(zip(patch_coeffs, importance)):
                # Importance-weighted keep ratio
                patch_keep_ratio = adjusted_keep_ratio * (0.5 + 0.5 * patch_importance)
                patch_keep_ratio = np.clip(patch_keep_ratio, 0.01, 0.95)
                
                # Select top coefficients
                num_keep = max(1, int(len(coeffs_patch) * patch_keep_ratio))
                coeff_importance = np.abs(coeffs_patch)
                top_indices = np.argsort(coeff_importance)[-num_keep:]
                
                compressed_coeffs[i, top_indices] = coeffs_patch[top_indices]
            
            scale_coefficients[scale] = compressed_coeffs
        
        return scale_coefficients
    
    def reconstruct_multiscale(self, 
                              scale_coefficients: Dict[int, np.ndarray],
                              multiscale_patches: Dict[int, Tuple[np.ndarray, List]],
                              original_shape: Tuple[int, int]) -> np.ndarray:
        """
        Reconstruct image from multi-scale coefficients.
        
        Args:
            scale_coefficients: Compressed coefficients for each scale
            multiscale_patches: Original patch position information
            original_shape: Shape of original image
            
        Returns:
            Reconstructed image
        """
        h, w = original_shape
        reconstruction = np.zeros((h, w))
        weight_map = np.zeros((h, w))
        
        # Process each scale
        for scale in sorted(scale_coefficients.keys(), reverse=True):  # Largest to smallest
            coeffs = scale_coefficients[scale]
            patches, positions = multiscale_patches[scale]
            
            # Reconstruct patches for this scale
            for i, (coeffs_patch, (pos_i, pos_j)) in enumerate(zip(coeffs, positions)):
                # Inverse DCT
                coeffs_2d = coeffs_patch.reshape(scale, scale)
                patch_recon = idct(idct(coeffs_2d, axis=0, norm='ortho'), axis=1, norm='ortho')
                
                # Add to reconstruction with appropriate weighting
                end_i = min(pos_i + scale, h)
                end_j = min(pos_j + scale, w)
                
                # Weight by scale (smaller scales have higher weight for detail)
                scale_weight = min(self.scales) / scale
                
                reconstruction[pos_i:end_i, pos_j:end_j] += patch_recon[:end_i-pos_i, :end_j-pos_j] * scale_weight
                weight_map[pos_i:end_i, pos_j:end_j] += scale_weight
        
        # Normalize by weights
        weight_map[weight_map == 0] = 1
        reconstruction = reconstruction / weight_map
        
        return np.clip(reconstruction, 0.0, 255.0)