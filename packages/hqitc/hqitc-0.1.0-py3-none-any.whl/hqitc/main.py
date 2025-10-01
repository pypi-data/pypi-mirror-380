# HQITC - Testable version (quantum bypass + quality-driven quantization + realistic entropy sim)
# Author: AI Research Implementation (revised)
# Date: September 2025 - Testable build

import numpy as np
import time

from .encoder import QuantumInspiredEncoder
from .utils import AttentionWaveletTransform, AdaptiveNeuralEntropyCoder
from .color import ColorSpaceProcessor
from .multiscale import MultiScaleAttentionTransform
from typing import Tuple, Dict, List, Optional
import warnings

warnings.filterwarnings('ignore')


class HQITCCompressor:
    def __init__(self, patch_size: int = 8, quantum_dim: int = 32,
                 embed_dim: int = 64, num_heads: int = 8, seed: int = 42,
                 use_quantum: bool = False, color_mode: str = 'auto',
                 use_multiscale: bool = False, multiscale_sizes: List[int] = None):
        self.patch_size = patch_size
        self.seed = seed
        self.use_quantum = use_quantum
        self.color_mode = color_mode  # 'auto', 'grayscale', 'color'
        self.use_multiscale = use_multiscale
        
        # Initialize components
        self.quantum_encoder = QuantumInspiredEncoder(patch_size, quantum_dim, seed)
        self.attention_wavelet = AttentionWaveletTransform(embed_dim, num_heads, seed)
        self.entropy_coder = AdaptiveNeuralEntropyCoder(seed=seed)
        self.color_processor = ColorSpaceProcessor()
        
        # Multi-scale attention setup
        if use_multiscale:
            if multiscale_sizes is None:
                # Default: use patch_size and adjacent scales
                if patch_size == 8:
                    multiscale_sizes = [4, 8, 16]
                elif patch_size == 4:
                    multiscale_sizes = [4, 8]
                elif patch_size == 16:
                    multiscale_sizes = [8, 16]
                else:
                    multiscale_sizes = [patch_size]
            self.multiscale_attention = MultiScaleAttentionTransform(multiscale_sizes, embed_dim, seed)
            self.multiscale_sizes = multiscale_sizes
        
        print("HQITC Compressor initialized:")
        print(f"  Patch size: {patch_size}x{patch_size}")
        print(f"  Quantum dimension: {quantum_dim}")
        print(f"  Attention heads: {num_heads}")
        print(f"  Embedding dimension: {embed_dim}")
        print(f"  Quantum encoder enabled: {self.use_quantum}")
        print(f"  Color mode: {color_mode}")
        print(f"  Multi-scale attention: {use_multiscale}")
        if use_multiscale:
            print(f"  Multi-scale sizes: {multiscale_sizes}")

    def extract_patches(self, image: np.ndarray) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
        if image.ndim != 2:
            raise ValueError("Expected 2D image")
        h, w = image.shape
        patches = []
        positions = []
        for i in range(0, h - self.patch_size + 1, self.patch_size):
            for j in range(0, w - self.patch_size + 1, self.patch_size):
                p = image[i:i + self.patch_size, j:j + self.patch_size]
                patches.append(p.flatten())
                positions.append((i, j))
        return np.array(patches), positions

    def reconstruct_from_patches(self, patches: np.ndarray, positions: List[Tuple[int, int]],
                                 original_shape: Tuple[int, int]) -> np.ndarray:
        reconstructed = np.zeros(original_shape, dtype=float)
        counts = np.zeros(original_shape, dtype=float)
        for p_flat, (i, j) in zip(patches, positions):
            p = p_flat.reshape(self.patch_size, self.patch_size)
            end_i = min(i + self.patch_size, original_shape[0])
            end_j = min(j + self.patch_size, original_shape[1])
            reconstructed[i:end_i, j:end_j] += p[:end_i - i, :end_j - j]
            counts[i:end_i, j:end_j] += 1
        counts[counts == 0] = 1
        return reconstructed / counts

    def compress(self, image: np.ndarray, quality_factor: float = 0.5, keep_ratio: float = 0.3,
                 verbose: bool = True) -> Dict:
        """
        Compress an image (grayscale or color).
        
        Args:
            image: Input image array. Can be 2D (grayscale) or 3D (RGB color)
            quality_factor: Quality control (0.0-1.0)
            keep_ratio: Base coefficient keep ratio
            verbose: Enable detailed logging
            
        Returns:
            Compressed data dictionary
        """
        # Determine if this is a color or grayscale image
        is_color = (image.ndim == 3 and image.shape[2] == 3)
        
        if is_color and self.color_mode != 'grayscale':
            return self._compress_color(image, quality_factor, keep_ratio, verbose)
        else:
            # Convert color to grayscale if needed
            if is_color:
                grayscale = np.mean(image, axis=2).astype(np.float32)
                if verbose:
                    print("Converting color image to grayscale")
            else:
                grayscale = image
            return self._compress_grayscale(grayscale, quality_factor, keep_ratio, verbose)
    
    def _compress_color(self, rgb_image: np.ndarray, quality_factor: float, keep_ratio: float, 
                       verbose: bool) -> Dict:
        """Compress a color RGB image using YUV color space."""
        t0 = time.time()
        if verbose:
            print("Starting HQITC color compression...")
            print(f"RGB Image shape: {rgb_image.shape}, quality_factor: {quality_factor}")
        
        # Convert to YUV color space
        yuv_channels = self.color_processor.rgb_to_yuv(rgb_image)
        
        # Compress each channel with different settings
        compressed_channels = {}
        channel_info = {}
        
        for channel_name, channel_image in yuv_channels.items():
            if verbose:
                print(f"\n--- Compressing {channel_name} channel ---")
            
            # Get channel-specific compression parameters
            ch_quality, ch_keep_ratio = self.color_processor.get_channel_compression_params(
                channel_name, quality_factor, keep_ratio
            )
            
            # Compress the channel
            channel_result = self._compress_grayscale(
                channel_image, ch_quality, ch_keep_ratio, verbose
            )
            
            compressed_channels[channel_name] = channel_result
            
            # Handle both single-scale and multi-scale results
            if 'encoding_info' in channel_result:
                # Single-scale compression
                coeffs_kept = channel_result['encoding_info']['num_nonzero']
                total_bits = channel_result['encoding_info']['total_bits']
            else:
                # Multi-scale compression
                coeffs_kept = sum(info['num_nonzero'] for info in channel_result['entropy_info_scales'].values())
                total_bits = channel_result['total_bits']
            
            channel_info[channel_name] = {
                'quality': ch_quality,
                'keep_ratio': ch_keep_ratio,
                'compression_ratio': channel_result['compression_ratio'],
                'coeffs_kept': coeffs_kept,
                'total_bits': total_bits
            }
        
        # Calculate overall compression metrics
        total_original_bits = rgb_image.size * 8  # 3 channels * 8 bits each
        total_compressed_bits = sum(
            ch_info['total_bits'] for ch_info in channel_info.values()
        )
        overall_compression_ratio = total_original_bits / max(total_compressed_bits, 1e-12)
        
        comp_time = time.time() - t0
        
        if verbose:
            print(f"\n--- Color Compression Summary ---")
            for channel, info in channel_info.items():
                print(f"{channel}: CR {info['compression_ratio']:.2f}:1, kept {info['coeffs_kept']} coeffs")
            print(f"Overall compression ratio: {overall_compression_ratio:.2f}:1")
            print(f"Total compression time: {comp_time:.4f}s")
        
        return {
            'type': 'color',
            'original_shape': rgb_image.shape,
            'channels': compressed_channels,
            'channel_info': channel_info,
            'compression_time': comp_time,
            'compression_ratio': overall_compression_ratio,
            'total_compressed_bits': total_compressed_bits
        }
    
    def _compress_grayscale(self, image: np.ndarray, quality_factor: float = 0.5, keep_ratio: float = 0.3,
                           verbose: bool = True) -> Dict:
        t0 = time.time()
        if verbose:
            mode_str = "multi-scale" if self.use_multiscale else "single-scale"
            print(f"Starting HQITC {mode_str} compression...")
            print(f"Image shape: {image.shape}, quality_factor: {quality_factor}, keep_ratio(base): {keep_ratio}")
        
        if self.use_multiscale:
            return self._compress_multiscale(image, quality_factor, keep_ratio, verbose, t0)
        else:
            return self._compress_singlescale(image, quality_factor, keep_ratio, verbose, t0)
    
    def _compress_multiscale(self, image: np.ndarray, quality_factor: float, keep_ratio: float, 
                            verbose: bool, t0: float) -> Dict:
        """Compress using multi-scale attention."""
        # Extract patches at multiple scales
        multiscale_patches = self.multiscale_attention.extract_multiscale_patches(image)
        
        if verbose:
            total_patches = sum(len(patches) for patches, _ in multiscale_patches.values())
            print(f"✓ Extracted {total_patches} patches across {len(multiscale_patches)} scales")
            for scale, (patches, _) in multiscale_patches.items():
                print(f"  Scale {scale}x{scale}: {len(patches)} patches")
        
        # Apply hierarchical attention
        multiscale_results = self.multiscale_attention.hierarchical_attention(multiscale_patches)
        if verbose:
            print("✓ Multi-scale attention computed")
        
        # Adaptive coefficient selection across scales
        scale_coefficients = self.multiscale_attention.adaptive_coefficient_selection_multiscale(
            multiscale_results, multiscale_patches, keep_ratio
        )
        
        if verbose:
            print("✓ Multi-scale coefficient selection complete")
        
        # Quantization and entropy coding for each scale
        quantized_scales = {}
        entropy_info_scales = {}
        total_bits = 64.0  # Header overhead
        
        quality_clamped = float(np.clip(quality_factor, 0.0, 1.0))
        
        for scale, coeffs in scale_coefficients.items():
            # Scale-specific quantization
            max_abs = float(np.max(np.abs(coeffs)) + 1e-12)
            base_step = max_abs / 128.0
            quality_multiplier = (1.0 - quality_clamped) * 10.0 + 1.0
            q_step = base_step * quality_multiplier
            q_step = np.clip(q_step, max_abs / 1000.0, max_abs / 2.0)
            
            # Quantize
            quantized = np.round(coeffs / (q_step + 1e-12)).astype(np.int32)
            
            # Entropy estimation
            entropy_info = self.entropy_coder.estimate_bits(quantized)
            
            quantized_scales[scale] = {
                'coeffs': quantized,
                'q_step': q_step,
                'coeffs_shape': coeffs.shape
            }
            entropy_info_scales[scale] = entropy_info
            total_bits += entropy_info['total_bits']
        
        # Calculate compression metrics
        original_bits = float(image.size) * 8.0
        compression_ratio = original_bits / max(total_bits, 1e-12)
        comp_time = time.time() - t0
        
        if verbose:
            total_coeffs = sum(info['num_nonzero'] for info in entropy_info_scales.values())
            print(f"✓ Selected {total_coeffs} total coefficients across all scales")
            print(f"✓ Total bits: {total_bits:.1f}, Compression ratio: {compression_ratio:.2f}:1")
            print(f"✓ Compression time: {comp_time:.4f}s")
        
        return {
            'type': 'multiscale',
            'quantized_scales': quantized_scales,
            'entropy_info_scales': entropy_info_scales,
            'multiscale_patches': multiscale_patches,  # Need for decompression
            'original_shape': image.shape,
            'compression_time': comp_time,
            'compression_ratio': compression_ratio,
            'total_bits': total_bits,
            'scales': self.multiscale_sizes,
            'params': {
                'quality_factor': quality_factor,
                'keep_ratio': keep_ratio,
                'use_quantum': self.use_quantum
            }
        }
    
    def _compress_singlescale(self, image: np.ndarray, quality_factor: float, keep_ratio: float,
                             verbose: bool, t0: float) -> Dict:
        """Compress using single-scale attention (original method)."""
        patches, positions = self.extract_patches(image)
        if verbose:
            print(f"✓ Extracted {len(patches)} patches")

        # Quantum or bypass
        if self.use_quantum:
            quantum_encoded = self.quantum_encoder.encode_patches(patches)
        else:
            # bypass: use raw patches (float) as embeddings (keeps signal intact)
            quantum_encoded = patches.astype(float)

        if verbose:
            print("✓ Quantum stage (bypass={}) complete".format(not self.use_quantum))

        # Attention
        attended_patches, patch_importance = self.attention_wavelet.multi_head_attention(quantum_encoded)
        if verbose:
            print("✓ Attention computed")

        # Apply DCT to each patch individually to preserve patch-level information
        patch_coeffs = []
        expected_patch_dim = self.patch_size * self.patch_size
        
        for i, patch in enumerate(attended_patches):
            # Handle dimension mismatch between attended patches and original patch size
            if patch.size >= expected_patch_dim:
                # Take the first patch_size^2 elements
                patch_data = patch[:expected_patch_dim]
            else:
                # Pad if attended patch is smaller (shouldn't happen in normal cases)
                patch_data = np.zeros(expected_patch_dim)
                patch_data[:patch.size] = patch
            
            # Reshape patch back to 2D for DCT
            patch_2d = patch_data.reshape(self.patch_size, self.patch_size)
            patch_dct = self.attention_wavelet.wavelet_transform_2d(patch_2d)
            patch_coeffs.append(patch_dct.flatten())
        
        patch_coeffs = np.array(patch_coeffs)  # Shape: (num_patches, patch_size^2)

        # Integrate quality_factor more reasonably
        quality_clamped = float(np.clip(quality_factor, 0.0, 1.0))
        effective_keep = float(keep_ratio) * (0.8 + 0.4 * quality_clamped)  # More conservative range
        effective_keep = float(np.clip(effective_keep, 0.01, 0.8))  # Don't go too extreme

        # Select important coefficients within each patch based on patch importance
        compressed_coeffs = np.zeros_like(patch_coeffs)
        important_indices = []
        
        for i, (coeffs_patch, importance) in enumerate(zip(patch_coeffs, patch_importance)):
            # Higher importance patches get to keep more coefficients
            patch_keep_ratio = effective_keep * (0.5 + 0.5 * importance)
            patch_keep_ratio = np.clip(patch_keep_ratio, 0.01, 0.95)
            
            # Select most important coefficients in this patch
            num_keep = max(1, int(len(coeffs_patch) * patch_keep_ratio))
            coeff_importance = np.abs(coeffs_patch)
            top_indices = np.argsort(coeff_importance)[-num_keep:]
            
            compressed_coeffs[i, top_indices] = coeffs_patch[top_indices]
            important_indices.extend([(i, j) for j in top_indices])

        # Flatten for quantization
        coeffs = compressed_coeffs  # Keep patch structure for now

        # Quantization step controlled by quality_factor
        max_abs = float(np.max(np.abs(coeffs)) + 1e-12)
        base_step = max_abs / 128.0  # Start with 1/128 of max value
        quality_multiplier = (1.0 - quality_clamped) * 10.0 + 1.0  # Range: 1.0 to 11.0
        q_step = base_step * quality_multiplier
        q_step = np.clip(q_step, max_abs / 1000.0, max_abs / 2.0)
        
        # Apply quantization to selected coefficients only (saves zeros)
        quantized = np.round(compressed_coeffs / (q_step + 1e-12)).astype(np.int32)

        # Entropy bit estimation on quantized representation
        entropy_info = self.entropy_coder.estimate_bits(quantized)

        # Realistic compression ratio: original bits = image.size * 8
        original_bits = float(image.size) * 8.0
        total_bits = float(entropy_info['total_bits']) + 64.0  # include small header overhead
        compression_ratio = original_bits / max(total_bits, 1e-12)

        comp_time = time.time() - t0
        if verbose:
            print(f"✓ Selected {entropy_info['num_nonzero']} nonzero quantized coeffs (~{effective_keep*100:.3f}% kept)")
            print(f"✓ q_step: {q_step:.6f}, bits_per_coeff_est: {entropy_info['bits_per_coeff']:.2f}")
            print(f"✓ Simulated total_bits: {total_bits:.1f}, Compression ratio: {compression_ratio:.2f}:1")
            print(f"✓ Compression time: {comp_time:.4f}s")

        return {
            'type': 'singlescale',
            'compressed_quantized': quantized,
            'q_step': q_step,
            'coeffs_shape': coeffs.shape,
            'patch_importance': patch_importance,
            'important_indices': important_indices,
            'original_shape': image.shape,
            'positions': positions,
            'encoding_info': entropy_info,
            'compression_time': comp_time,
            'compression_ratio': compression_ratio,
            'params': {
                'quality_factor': quality_factor,
                'keep_ratio': keep_ratio,
                'effective_keep': effective_keep,
                'use_quantum': self.use_quantum
            }
        }

        # Select important coefficients within each patch based on patch importance
        compressed_coeffs = np.zeros_like(patch_coeffs)
        important_indices = []
        
        for i, (coeffs_patch, importance) in enumerate(zip(patch_coeffs, patch_importance)):
            # Higher importance patches get to keep more coefficients
            patch_keep_ratio = effective_keep * (0.5 + 0.5 * importance)
            patch_keep_ratio = np.clip(patch_keep_ratio, 0.01, 0.95)
            
            # Select most important coefficients in this patch
            num_keep = max(1, int(len(coeffs_patch) * patch_keep_ratio))
            coeff_importance = np.abs(coeffs_patch)
            top_indices = np.argsort(coeff_importance)[-num_keep:]
            
            compressed_coeffs[i, top_indices] = coeffs_patch[top_indices]
            important_indices.extend([(i, j) for j in top_indices])

        # Flatten for quantization
        coeffs = compressed_coeffs  # Keep patch structure for now

        # Quantization step controlled by quality_factor
        # Higher quality -> smaller q_step -> less loss
        max_abs = float(np.max(np.abs(coeffs)) + 1e-12)
        
        # More reasonable quantization step calculation
        # Base step size should be proportional to signal range
        base_step = max_abs / 128.0  # Start with 1/128 of max value
        
        # Quality factor controls how much to increase this step
        # quality=1.0 -> minimal quantization, quality=0.0 -> heavy quantization
        quality_multiplier = (1.0 - quality_clamped) * 10.0 + 1.0  # Range: 1.0 to 11.0
        q_step = base_step * quality_multiplier
        
        # Ensure reasonable bounds
        q_step = np.clip(q_step, max_abs / 1000.0, max_abs / 2.0)
        
        # Apply quantization to selected coefficients only (saves zeros)
        quantized = np.round(compressed_coeffs / (q_step + 1e-12)).astype(np.int32)

        # Entropy bit estimation on quantized representation
        entropy_info = self.entropy_coder.estimate_bits(quantized)

        # Realistic compression ratio: original bits = image.size * 8
        original_bits = float(image.size) * 8.0
        total_bits = float(entropy_info['total_bits']) + 64.0  # include small header overhead
        compression_ratio = original_bits / max(total_bits, 1e-12)

        comp_time = time.time() - t0
        if verbose:
            print(f"✓ Selected {entropy_info['num_nonzero']} nonzero quantized coeffs (~{effective_keep*100:.3f}% kept)")
            print(f"✓ q_step: {q_step:.6f}, bits_per_coeff_est: {entropy_info['bits_per_coeff']:.2f}")
            print(f"✓ Simulated total_bits: {total_bits:.1f}, Compression ratio: {compression_ratio:.2f}:1")
            print(f"✓ Compression time: {comp_time:.4f}s")

        return {
            'compressed_quantized': quantized,
            'q_step': q_step,
            'coeffs_shape': coeffs.shape,
            'patch_importance': patch_importance,
            'important_indices': important_indices,
            'original_shape': image.shape,
            'positions': positions,
            'encoding_info': entropy_info,
            'compression_time': comp_time,
            'compression_ratio': compression_ratio,
            'params': {
                'quality_factor': quality_factor,
                'keep_ratio': keep_ratio,
                'effective_keep': effective_keep,
                'use_quantum': self.use_quantum
            }
        }

    def decompress(self, compressed_data: Dict, verbose: bool = True) -> np.ndarray:
        """
        Decompress compressed data back to image.
        
        Args:
            compressed_data: Compressed data dictionary
            verbose: Enable detailed logging
            
        Returns:
            Reconstructed image array
        """
        # Check if this is color or grayscale data
        if compressed_data.get('type') == 'color':
            return self._decompress_color(compressed_data, verbose)
        else:
            return self._decompress_grayscale(compressed_data, verbose)
    
    def _decompress_color(self, compressed_data: Dict, verbose: bool = True) -> np.ndarray:
        """Decompress color image data."""
        t0 = time.time()
        if verbose:
            print("Starting HQITC color decompression...")
        
        # Decompress each YUV channel
        yuv_channels = {}
        channels_data = compressed_data['channels']
        
        for channel_name in ['Y', 'U', 'V']:
            if verbose:
                print(f"Decompressing {channel_name} channel...")
            
            channel_result = self._decompress_grayscale(channels_data[channel_name], verbose=False)
            yuv_channels[channel_name] = channel_result
        
        # Convert back to RGB
        rgb_image = self.color_processor.yuv_to_rgb(yuv_channels)
        
        dt = time.time() - t0
        if verbose:
            print(f"✓ Color decompression done in {dt:.4f}s")
        
        return rgb_image
    
    def _decompress_grayscale(self, compressed_data: Dict, verbose: bool = True) -> np.ndarray:
        """Decompress grayscale image data."""
        # Check if this is multi-scale or single-scale data
        if compressed_data.get('type') == 'multiscale':
            return self._decompress_multiscale(compressed_data, verbose)
        else:
            return self._decompress_singlescale(compressed_data, verbose)
    
    def _decompress_multiscale(self, compressed_data: Dict, verbose: bool = True) -> np.ndarray:
        """Decompress multi-scale data."""
        t0 = time.time()
        if verbose:
            print("Starting HQITC multi-scale decompression...")
        
        quantized_scales = compressed_data['quantized_scales']
        multiscale_patches = compressed_data['multiscale_patches']
        original_shape = tuple(compressed_data['original_shape'])
        
        # Dequantize each scale
        scale_coefficients = {}
        for scale, scale_data in quantized_scales.items():
            quantized = scale_data['coeffs']
            q_step = scale_data['q_step']
            
            # Dequantize
            dequant = (quantized.astype(float)) * q_step
            scale_coefficients[scale] = dequant
        
        if verbose:
            print(f"✓ Dequantized {len(scale_coefficients)} scales")
        
        # Reconstruct using multi-scale approach
        reconstructed = self.multiscale_attention.reconstruct_multiscale(
            scale_coefficients, multiscale_patches, original_shape
        )
        
        dt = time.time() - t0
        if verbose:
            print(f"✓ Multi-scale decompression done in {dt:.4f}s")
        
        return reconstructed
    
    def _decompress_singlescale(self, compressed_data: Dict, verbose: bool = True) -> np.ndarray:
        """Decompress single-scale data.""" 
        t0 = time.time()
        if verbose:
            print("Starting HQITC decompression...")
            
        quantized = compressed_data['compressed_quantized']
        q_step = float(compressed_data['q_step'])
        coeffs_shape = tuple(compressed_data['coeffs_shape'])
        positions = compressed_data['positions']
        original_shape = tuple(compressed_data['original_shape'])
        
        # Dequantize
        dequant = (quantized.astype(float)) * q_step
        
        # Reconstruct patches from DCT coefficients
        reconstructed_patches = []
        
        # dequant should have shape (num_patches, patch_size^2)
        for i, patch_coeffs in enumerate(dequant):
            # Reshape coefficients back to 2D for inverse DCT
            coeffs_2d = patch_coeffs.reshape(self.patch_size, self.patch_size)
            
            # Apply inverse DCT
            patch_recon = self.attention_wavelet.inverse_wavelet_transform_2d(coeffs_2d)
            
            # Flatten for reconstruction
            reconstructed_patches.append(patch_recon.flatten())
        
        reconstructed_patches = np.array(reconstructed_patches)
        
        # Reconstruct full image from patches
        recon = self.reconstruct_from_patches(reconstructed_patches, positions, original_shape)
        recon = np.clip(recon, 0.0, 255.0)
        
        dt = time.time() - t0
        if verbose:
            print(f"✓ Decompression done in {dt:.4f}s")
        return recon


# ---------- Demo / quick test ----------
def make_test_images(size=128):
    imgs = {}
    n = size
    x = np.indices((n, n))[0]
    y = np.indices((n, n))[1]
    checker = ((x // 8) % 2) ^ ((y // 8) % 2)
    imgs['geometric'] = (checker * 255).astype(np.float32)
    xv, yv = np.meshgrid(np.linspace(0, 8 * np.pi, n), np.linspace(0, 8 * np.pi, n))
    tex = (np.sin(xv * 2.3) + np.sin(yv * 3.7) + np.sin((xv + yv) * 1.9))
    tex = (tex - tex.min()) / (tex.max() - tex.min()) * 255
    imgs['texture'] = tex.astype(np.float32)
    cx, cy = n // 2, n // 2
    r = n // 3
    dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    edges = (np.abs(dist - r) < 2).astype(float) * 255
    imgs['edges'] = edges.astype(np.float32)
    grad = np.tile(np.linspace(0, 255, n), (n, 1))
    imgs['gradient'] = grad.astype(np.float32)
    return imgs


if __name__ == "__main__":
    compressor = HQITCCompressor(patch_size=8, quantum_dim=32, embed_dim=64, num_heads=8, seed=42, use_quantum=False)

    tests = make_test_images(128)
    summary = {}
    for name, img in tests.items():
        print("\n" + "-" * 60)
        print(f"Testing image: {name.upper()} {img.shape}")
        res = compressor.compress(img, quality_factor=0.6, keep_ratio=0.15, verbose=True)
        recon = compressor.decompress(res, verbose=True)
        mse = np.mean((img - recon) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        def ssim_sur(a, b):
            am, bm = a.mean(), b.mean()
            cov = ((a - am) * (b - bm)).mean()
            va = ((a - am) ** 2).mean()
            vb = ((b - bm) ** 2).mean()
            return (2 * cov + 1e-6) / (va + vb + 1e-6)
        ssim_val = ssim_sur(img, recon)
        print(f"PSNR: {psnr:.2f} dB, SSIM-surrogate: {ssim_val:.6f}")
        summary[name] = {'psnr': psnr, 'ssim': ssim_val, 'cr': res['compression_ratio'], 'kept': res['encoding_info']['num_nonzero']}

    print("\nSUMMARY")
    for k, v in summary.items():
        print(f"{k}: PSNR {v['psnr']:.2f} dB, SSIM {v['ssim']:.6f}, CR {v['cr']:.2f}:1, kept {v['kept']} coeffs")
