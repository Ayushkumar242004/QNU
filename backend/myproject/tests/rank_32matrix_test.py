import numpy as np
from scipy.stats import chi2

class Ranks32x32MatricesTest:
    @staticmethod
    def Ranks32x32MatricesTest(data, verbose=False):
        if len(data) < 31 * 31:
            return -1, False  # Return (-1, False) if insufficient data
        
        
        n = len(data) // (32 * 32)  # Number of 32x32 matrices
        counts = np.zeros(3)  # For rank 32, 31, and less
        
        for i in range(n):
            matrix = np.reshape(data[i * 32 * 32:(i + 1) * 32 * 32], (32, 32))
            rank = np.linalg.matrix_rank(matrix)
            if rank == 32:
                counts[0] += 1
            elif rank == 31:
                counts[1] += 1
            else:
                counts[2] += 1

        # Expected proportions for rank 32, 31, and less
        expected_proportions = np.array([0.3230, 0.5744, 0.1026])
        expected_counts = n * expected_proportions

        chi_square = np.sum((counts - expected_counts) ** 2 / expected_counts)
        p_value = 1 - chi2.cdf(chi_square, 2)

        if verbose:
            print(f"Ranks 32x32 Matrices Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
