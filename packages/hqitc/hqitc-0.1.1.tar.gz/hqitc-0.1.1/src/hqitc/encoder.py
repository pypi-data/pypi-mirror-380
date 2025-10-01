import numpy as np

class QuantumInspiredEncoder:
    def __init__(self, patch_size: int = 8, quantum_dim: int = 64, seed: int = 42):
        self.patch_size = patch_size
        self.quantum_dim = quantum_dim
        np.random.seed(seed)
        patch_dim = patch_size * patch_size
        xavier_scale = np.sqrt(2.0 / (patch_dim + quantum_dim))
        self.amplitude_weights = np.random.randn(patch_dim, quantum_dim) * xavier_scale
        self.phase_weights = np.random.randn(patch_dim, quantum_dim) * xavier_scale
        self.unitary_real = np.random.randn(quantum_dim, quantum_dim) * xavier_scale
        self.unitary_imag = np.random.randn(quantum_dim, quantum_dim) * xavier_scale
        self.reconstruction_weights = np.random.randn(quantum_dim * 2, patch_dim) * xavier_scale
        self.phase_scale = 2 * np.pi

    def create_unitary_matrix(self) -> np.ndarray:
        U_complex = self.unitary_real + 1j * self.unitary_imag
        Q, _ = np.linalg.qr(U_complex)
        return Q

    def encode_patches(self, patches: np.ndarray) -> np.ndarray:
        # Keep shape (num_patches, patch_dim)
        patches_normalized = patches / 255.0
        amplitudes = np.tanh(patches_normalized @ self.amplitude_weights)
        phases = (1 / (1 + np.exp(-patches_normalized @ self.phase_weights))) * self.phase_scale
        quantum_state = amplitudes * np.exp(1j * phases)
        U = self.create_unitary_matrix()
        evolved_state = quantum_state @ U
        measured_real = evolved_state.real
        measured_imag = evolved_state.imag
        measured_combined = np.concatenate([measured_real, measured_imag], axis=-1)
        reconstructed = measured_combined @ self.reconstruction_weights
        reconstructed = reconstructed * 255.0
        reconstructed = np.clip(reconstructed, 0.0, 255.0)
        return reconstructed