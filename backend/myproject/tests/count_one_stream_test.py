import numpy as np
from scipy.stats import norm
from math import sqrt

class CountThe1sStreamTest:
    @staticmethod
    def CountThe1sStreamTest(data, verbose=False):
        # Clean and convert input data to integers
        try:
            # Split the data by commas and filter out invalid entries
            data = [int(x) for x in data.split(',') if x.strip().isdigit() and x.strip() in ('0', '1')]
            data = np.array(data, dtype=int)  # Convert to numpy array of integers
            
            if data.size == 0:
                raise ValueError("Input data must contain valid binary values (0s and 1s).")
            
            n = len(data)
            ones_count = np.sum(data)  # Count the number of 1s in the data
            expected = n / 2  # Expected number of 1s if the data is random
            variance = n / 4  # Variance for a binomial distribution (n/4 for p=0.5)
            z_statistic = (ones_count - expected) / sqrt(variance)  # Z-statistic calculation
            p_value = 2 * (1 - norm.cdf(abs(z_statistic)))  # Two-tailed p-value
            
            if verbose:
                print(f"Count-the-1s (Stream) Test - Z-statistic: {z_statistic}, p-value: {p_value}")
            
            return p_value, (p_value >= 0.01)  # Return p-value and boolean for pass/fail

        except ValueError as e:
            print(f"ValueError: {e}")
            return -1, False  # Return -1 if there's a ValueError
        except OverflowError as e:
            print(f"OverflowError: {e}")
            return -1, False  # Return -1 and False if there's an overflow error
