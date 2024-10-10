import numpy as np
from scipy.stats import chi2

class Ranks31x31MatricesTest:
    @staticmethod
    def Ranks31x31MatricesTest(data, verbose=False):
        # Check if data has at least 31x31 elements
        if len(data) < 31 * 31:
            return -1, False  # Return (-1, False) if insufficient data

        try:
            # Ensure data consists of integers (handling any non-integer characters)
            data = [int(bit) for bit in data]
        except ValueError:
            return -1, False  # Return (-1, False) if conversion to int fails

        n = len(data) // (31 * 31)  # Number of 31x31 matrices
        counts = np.zeros(3)  # For rank 31, 30, and less

        for i in range(n):
            matrix_data = data[i * 31 * 31:(i + 1) * 31 * 31]
            matrix = np.reshape(matrix_data, (31, 31))
            rank = np.linalg.matrix_rank(matrix)

            if rank == 31:
                counts[0] += 1
            elif rank == 30:
                counts[1] += 1
            else:
                counts[2] += 1

        # Debugging: print counts
        print(f"Counts: {counts}")

        # Expected proportions for rank 31, 30, and less
        expected_proportions = np.array([0.2888, 0.5776, 0.1336])
        expected_counts = n * expected_proportions

        # Chi-square test
        chi_square = np.sum((counts - expected_counts) ** 2 / expected_counts)
        p_value = 1 - chi2.cdf(chi_square, 2)

        if verbose:
            print(f"Ranks 31x31 Matrices Test - Chi-square: {chi_square}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)

