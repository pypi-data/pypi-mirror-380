"""
Command-line interface for HQITC compression algorithm.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import numpy as np
from PIL import Image

from .main import HQITCCompressor


def load_image(image_path: Path) -> np.ndarray:
    """Load and convert image to grayscale numpy array."""
    try:
        with Image.open(image_path) as img:
            # Convert to grayscale
            gray_img = img.convert('L')
            return np.array(gray_img, dtype=np.float32)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        sys.exit(1)


def save_image(image_array: np.ndarray, output_path: Path) -> None:
    """Save numpy array as image."""
    try:
        # Ensure values are in valid range
        image_array = np.clip(image_array, 0, 255).astype(np.uint8)
        img = Image.fromarray(image_array, mode='L')
        img.save(output_path)
    except Exception as e:
        print(f"Error saving image {output_path}: {e}")
        sys.exit(1)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="HQITC - Hybrid Quantum-Inspired Transform Codec",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  hqitc compress input.jpg -o compressed.hqitc -q 0.8
  hqitc decompress compressed.hqitc -o output.jpg
  hqitc demo  # Run demo with test images
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Compress command
    compress_parser = subparsers.add_parser('compress', help='Compress an image')
    compress_parser.add_argument('input', type=Path, help='Input image file')
    compress_parser.add_argument('-o', '--output', type=Path, required=True, 
                                help='Output compressed file')
    compress_parser.add_argument('-q', '--quality', type=float, default=0.6,
                                help='Quality factor (0.0-1.0, default: 0.6)')
    compress_parser.add_argument('-k', '--keep-ratio', type=float, default=0.15,
                                help='Coefficient keep ratio (default: 0.15)')
    compress_parser.add_argument('-v', '--verbose', action='store_true',
                                help='Verbose output')
    
    # Decompress command
    decompress_parser = subparsers.add_parser('decompress', help='Decompress an image')
    decompress_parser.add_argument('input', type=Path, help='Input compressed file')
    decompress_parser.add_argument('-o', '--output', type=Path, required=True,
                                  help='Output image file')
    decompress_parser.add_argument('-v', '--verbose', action='store_true',
                                  help='Verbose output')
    
    # Demo command
    demo_parser = subparsers.add_parser('demo', help='Run demo with test images')
    demo_parser.add_argument('-s', '--size', type=int, default=128,
                            help='Test image size (default: 128)')
    demo_parser.add_argument('-q', '--quality', type=float, default=0.6,
                            help='Quality factor (default: 0.6)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize compressor
    compressor = HQITCCompressor(
        patch_size=8,
        quantum_dim=32,
        embed_dim=64,
        num_heads=8,
        seed=42,
        use_quantum=False
    )
    
    if args.command == 'compress':
        compress_image(compressor, args)
    elif args.command == 'decompress':
        decompress_image(compressor, args)
    elif args.command == 'demo':
        run_demo(compressor, args)


def compress_image(compressor: HQITCCompressor, args) -> None:
    """Compress a single image."""
    print(f"Loading image: {args.input}")
    image = load_image(args.input)
    
    print(f"Compressing with quality={args.quality}, keep_ratio={args.keep_ratio}")
    result = compressor.compress(
        image, 
        quality_factor=args.quality,
        keep_ratio=args.keep_ratio,
        verbose=args.verbose
    )
    
    # Save compressed data (in practice, this would be a proper binary format)
    np.savez_compressed(args.output, **result)
    
    print(f"Compressed data saved to: {args.output}")
    print(f"Compression ratio: {result['compression_ratio']:.2f}:1")


def decompress_image(compressor: HQITCCompressor, args) -> None:
    """Decompress a compressed file."""
    print(f"Loading compressed data: {args.input}")
    
    try:
        compressed_data = dict(np.load(args.input))
    except Exception as e:
        print(f"Error loading compressed data: {e}")
        sys.exit(1)
    
    print("Decompressing...")
    reconstructed = compressor.decompress(compressed_data, verbose=args.verbose)
    
    save_image(reconstructed, args.output)
    print(f"Decompressed image saved to: {args.output}")


def run_demo(compressor: HQITCCompressor, args) -> None:
    """Run demo with test images."""
    from .main import make_test_images
    
    print("Running HQITC Demo")
    print("=" * 50)
    
    tests = make_test_images(args.size)
    summary = {}
    
    for name, img in tests.items():
        print(f"\nTesting image: {name.upper()} {img.shape}")
        print("-" * 40)
        
        result = compressor.compress(
            img, 
            quality_factor=args.quality, 
            keep_ratio=0.15, 
            verbose=True
        )
        
        recon = compressor.decompress(result, verbose=True)
        
        # Calculate metrics
        mse = np.mean((img - recon) ** 2)
        psnr = 10 * np.log10((255.0 ** 2) / (mse + 1e-12))
        
        def ssim_surrogate(a, b):
            am, bm = a.mean(), b.mean()
            cov = ((a - am) * (b - bm)).mean()
            va = ((a - am) ** 2).mean()
            vb = ((b - bm) ** 2).mean()
            return (2 * cov + 1e-6) / (va + vb + 1e-6)
        
        ssim_val = ssim_surrogate(img, recon)
        
        print(f"PSNR: {psnr:.2f} dB, SSIM: {ssim_val:.6f}")
        summary[name] = {
            'psnr': psnr, 
            'ssim': ssim_val, 
            'cr': result['compression_ratio'], 
            'coeffs': result['encoding_info']['num_nonzero']
        }
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    for name, metrics in summary.items():
        print(f"{name:10s}: PSNR {metrics['psnr']:6.2f} dB, "
              f"SSIM {metrics['ssim']:8.6f}, "
              f"CR {metrics['cr']:7.2f}:1, "
              f"coeffs {metrics['coeffs']:4d}")


if __name__ == "__main__":
    main()