class TestU01MatrixRankTest:
    @staticmethod
    def TestU01MatrixRankTest(data, m=32, verbose=False):
        # Ensure there is enough data to form matrices
        if len(data) < m * m:
            print(f"Not enough data to create {m}x{m} matrices.")
            return -1, False

        n = len(data) // (m * m)  # Number of matrices

        # Reshape only if there is enough data
        try:
            matrices = np.reshape(data[:n * m * m], (n, m, m))
        except ValueError as e:
            print(f"Error during reshaping: {e}")
            return -1, False

        ranks = np.array([np.linalg.matrix_rank(matrix) for matrix in matrices])

        full_rank = np.sum(ranks == m)
        expected = 0.2888 * n  # Approximation for 32x32 matrices
        variance = n * 0.2888 * (1 - 0.2888)
        z_statistic = (full_rank - expected) / sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Matrix Rank Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)
