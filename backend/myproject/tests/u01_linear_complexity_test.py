from math import sqrt
from scipy.stats import norm
import numpy as np

class TestU01LinearComplexityTest:
    @staticmethod
    def TestU01LinearComplexityTest(data, m=500, verbose=False):
        n = len(data)
        block_count = n // m
        blocks = [data[i * m:(i + 1) * m] for i in range(block_count)]
        complexities = [np.linalg.matrix_rank(np.array(block).reshape(m, -1)) for block in blocks]
        mean_complexity = np.mean(complexities)
        expected = m / 2
        variance = m * (1 / 2) * (1 - 1 / 2)
        z_statistic = (mean_complexity - expected) / sqrt(variance / block_count)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Linear Complexity Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
