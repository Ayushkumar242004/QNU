import numpy as np
from scipy.stats import norm
from math import sqrt

class CountThe1sStreamTest:
    @staticmethod
    def CountThe1sStreamTest(data, verbose=False):
        # Step 1: Sanitize input data
        data = data.replace(',', '').strip()
        
        if not data:
            return None 
        
        # Step 2: Initialize counters
        ones_count = 0
        total_count = 0

        # Step 3: Process the input data in a streaming manner
        for bit in data.split():  # Assuming space-separated or comma-separated input
            if bit in ('0', '1'):
                if bit == '1':
                    ones_count += 1
                total_count += 1
        
        if total_count == 0:
            return -1, False  # Handle case when no valid bits were processed
        
        # Step 4: Calculate statistical values
        expected = total_count / 2
        variance = total_count / 4  # Variance for a binomial distribution (n/4 for p=0.5)
        
        # Step 5: Handle edge cases for variance
        if variance <= 0:
            return -1, False  # Variance must be positive
        
        z_statistic = (ones_count - expected) / sqrt(variance)  # Z-statistic calculation
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))  # Two-tailed p-value

        # Step 6: Optional verbose output for debugging
        if verbose:
            print(f"Count-the-1s (Stream) Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        # Step 7: Return the p-value and result based on a significance level of 0.01
        return p_value, (p_value >= 0.01)

