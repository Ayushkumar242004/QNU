from math import sqrt
from scipy.stats import norm
import numpy as np

class TestU01LinearComplexityTest:
    @staticmethod
    def TestU01LinearComplexityTest(data, m=500, verbose=False):
        try:
            # Ensure the input data length is sufficient for block size 'm'
            n = len(data)
            if n < m:
                return -1, False  # Not enough data for even one block

            # Compute block count
            block_count = n // m
            if block_count == 0:
                return -1, False  # Prevent division by zero

            # Split data into blocks of size 'm'
            blocks = [data[i * m:(i + 1) * m] for i in range(block_count)]
            
            # Compute the linear complexity (rank) of each block
            complexities = [np.linalg.matrix_rank(np.array(block).reshape(m, -1)) for block in blocks]
            mean_complexity = np.mean(complexities)

            # Expected values and variance for the test
            expected = m / 2
            variance = m * (1 / 2) * (1 - 1 / 2)

            # Calculate Z-statistic
            z_statistic = (mean_complexity - expected) / sqrt(variance / block_count)
            p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

            if verbose:
                print(f"Linear Complexity Test - Z-statistic: {z_statistic}, p-value: {p_value}")
            
            # Return p-value and pass/fail result
            return p_value, (p_value >= 0.01)

        except ZeroDivisionError:
            print("Error: Block count or variance is zero, cannot divide.")
            return -1, False  # Return -1 for any division errors
        except Exception as e:
            print(f"Error: {e}")
            return -1, False  # Return -1 for any other error
