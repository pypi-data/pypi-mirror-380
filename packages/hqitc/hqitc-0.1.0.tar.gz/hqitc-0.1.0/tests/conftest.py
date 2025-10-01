"""Test configuration and fixtures for HQITC tests."""

import pytest
import numpy as np
from hqitc import HQITCCompressor


@pytest.fixture
def compressor():
    """Create a standard HQITC compressor instance."""
    return HQITCCompressor(
        patch_size=8,
        quantum_dim=32,
        embed_dim=64,
        num_heads=8,
        seed=42,
        use_quantum=False
    )


@pytest.fixture
def test_image():
    """Create a simple test image."""
    # Create a simple checkerboard pattern
    size = 64
    x, y = np.meshgrid(range(size), range(size))
    checker = ((x // 8) % 2) ^ ((y // 8) % 2)
    return (checker * 255).astype(np.float32)


@pytest.fixture
def gradient_image():
    """Create a gradient test image."""
    size = 64
    gradient = np.tile(np.linspace(0, 255, size), (size, 1))
    return gradient.astype(np.float32)