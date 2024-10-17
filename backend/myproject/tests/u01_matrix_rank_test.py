import numpy as np
from scipy.stats import norm  # For normal distribution
from math import sqrt

class TestU01MatrixRankTest:
    @staticmethod
    def TestU01MatrixRankTest(data, m=32, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Ensure there is enough data to form matrices
        if len(data) < m * m:
            return -1, False

        n = len(data) // (m * m)  # Number of matrices
        
        full_rank_count = 0  # To keep count of full rank matrices

        # Process data in chunks to avoid excessive memory usage
        for i in range(n):
            start_index = i * m * m
            end_index = start_index + m * m
            matrix_data = data[start_index:end_index]

            # Convert the chunk to a numpy array and reshape it into a matrix
            matrix = np.array(list(map(int, matrix_data))).reshape(m, m)
            rank = np.linalg.matrix_rank(matrix)  # Compute the rank of the matrix
            
            if rank == m:
                full_rank_count += 1  # Count if it's a full rank matrix

        expected = 0.2888 * n  # Approximation for 32x32 matrices
        variance = n * 0.2888 * (1 - 0.2888)
        z_statistic = (full_rank_count - expected) / sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Matrix Rank Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)

