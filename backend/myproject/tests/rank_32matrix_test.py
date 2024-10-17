import numpy as np
from scipy.stats import chi2

class Ranks32x32MatricesTest:
    @staticmethod
    def Ranks32x32MatricesTest(data, verbose=False):
        # Step 1: Sanitize input by removing commas and spaces
        data = data.replace(',', '').strip()

        if not data:
            return None 
        

        # Step 2: Check if there is enough data for at least one 32x32 matrix
        if len(data) < 32 * 32:
            return -1, False  # Insufficient data, return failure
        
        # Step 3: Convert binary string to integer data using NumPy for efficiency
        try:
            data = np.array(list(map(int, data)), dtype=np.int8)
        except ValueError:
            return -1, False  # Invalid data, return failure
        
        # Step 4: Calculate number of matrices
        n = len(data) // (32 * 32)
        if n == 0:
            return -1, False  # No valid matrices, return failure

        counts = np.zeros(3)  # For rank 32, 31, and less than 31

        # Step 5: Process the matrices in chunks to optimize memory usage
        for i in range(n):
            # Extract a 32x32 matrix from the binary data
            matrix = data[i * 32 * 32:(i + 1) * 32 * 32].reshape((32, 32))

            # Compute the rank of the matrix
            rank = np.linalg.matrix_rank(matrix)
            if rank == 32:
                counts[0] += 1
            elif rank == 31:
                counts[1] += 1
            else:
                counts[2] += 1

        # Step 6: Expected counts based on known rank proportions
        expected_proportions = np.array([0.3230, 0.5744, 0.1026])
        expected_counts = n * expected_proportions

        # Step 7: Chi-square test for goodness of fit
        chi_square = np.sum((counts - expected_counts) ** 2 / expected_counts)
        p_value = 1 - chi2.cdf(chi_square, 2)

        # Step 8: Optional verbose output for debugging
        if verbose:
            print(f"Ranks 32x32 Matrices Test - Chi-square: {chi_square}, p-value: {p_value}")

        # Step 9: Return the p-value and the test result based on a significance level of 0.01
        return p_value, (p_value >= 0.01)
