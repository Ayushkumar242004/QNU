import numpy as np
from scipy.stats import norm
from math import gcd  # Import gcd from the math module

class MarsagliaTsangGCDTest:
    @staticmethod
    def MarsagliaTsangGCDTest(data, verbose=False):
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 2:
            return -1, False  # Return (-1, False) if insufficient data for GCD calculation
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)  # Convert to integer array
        
        # Calculate GCD of consecutive elements
        gcd_values = np.array([gcd(data_array[i], data_array[i + 1]) for i in range(n - 1)])
        
        expected = 1.0
        sample_mean = np.mean(gcd_values)
        variance = np.var(gcd_values)

        # Avoid division by zero
        if variance == 0:
            return 0.0, False  # Return default values if variance is zero
        
        z_statistic = (sample_mean - expected) / np.sqrt(variance / (n - 1))  # Corrected degrees of freedom
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Marsaglia-Tsang GCD Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)

