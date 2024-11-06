import numpy as np
from scipy.stats import chi2
from concurrent.futures import ProcessPoolExecutor, as_completed

class Ranks32x32MatricesTest:
    @staticmethod
    def process_matrix(matrix_data):
        """
        Helper function to calculate the rank of a 32x32 matrix.
        Returns a tuple indicating counts of ranks 32, 31, and less than 31.
        """
        matrix = matrix_data.reshape((32, 32))
        rank = np.linalg.matrix_rank(matrix)
        if rank == 32:
            return (1, 0, 0)  # Count for rank 32
        elif rank == 31:
            return (0, 1, 0)  # Count for rank 31
        else:
            return (0, 0, 1)  # Count for less than rank 31

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

        # Step 5: Process the matrices in parallel
        with ProcessPoolExecutor() as executor:
            futures = []
            for i in range(n):
                # Extract a 32x32 matrix from the binary data
                matrix = data[i * 32 * 32:(i + 1) * 32 * 32]
                futures.append(executor.submit(Ranks32x32MatricesTest.process_matrix, matrix))

            for future in as_completed(futures):
                rank_counts = future.result()
                counts += rank_counts  # Accumulate counts for each rank

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
