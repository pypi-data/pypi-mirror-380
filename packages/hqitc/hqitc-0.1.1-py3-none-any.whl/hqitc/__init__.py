"""
HQITC - Hybrid Quantum-Inspired Transform Codec

A novel image compression algorithm combining quantum-inspired encoding,
attention mechanisms, and adaptive DCT transforms.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .encoder import QuantumInspiredEncoder
from .utils import AttentionWaveletTransform, AdaptiveNeuralEntropyCoder
from .color import ColorSpaceProcessor
from .multiscale import MultiScaleAttentionTransform
from .main import HQITCCompressor

__all__ = [
    "QuantumInspiredEncoder",
    "AttentionWaveletTransform", 
    "AdaptiveNeuralEntropyCoder",
    "ColorSpaceProcessor",
    "MultiScaleAttentionTransform",
    "HQITCCompressor",
]
