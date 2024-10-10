from math import sqrt
from scipy.stats import norm
import numpy as np

class TestU01MatrixRankTest:
    @staticmethod
    def TestU01MatrixRankTest(data, m=32, verbose=False):
        n = len(data) // (m * m)  # Number of matrices
        matrices = np.reshape(data[:n * m * m], (n, m, m))
        ranks = np.array([np.linalg.matrix_rank(matrix) for matrix in matrices])

        full_rank = np.sum(ranks == m)
        expected = 0.2888 * n  # Approximation from the literature for 32x32 matrices
        variance = n * 0.2888 * (1 - 0.2888)
        z_statistic = (full_rank - expected) / sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Matrix Rank Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
