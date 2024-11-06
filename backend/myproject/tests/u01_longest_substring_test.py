from math import sqrt
from scipy.stats import norm
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class TestU01LongestRepeatedSubstringTest:
    @staticmethod
    def compute_longest_repeated_length(substring, data):
        return len(substring) if data.count(substring) > 1 else 0

    @staticmethod
    def TestU01LongestRepeatedSubstringTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 

        # Generate all unique substrings
        unique_substrings = set(data)

        # Use ThreadPoolExecutor to compute longest repeated substring lengths in parallel
        longest_repeat = 0
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(TestU01LongestRepeatedSubstringTest.compute_longest_repeated_length, substring, data): substring for substring in unique_substrings}
            for future in as_completed(futures):
                longest_repeat = max(longest_repeat, future.result())

        expected = np.log2(len(data)) if len(data) > 0 else 0
        variance = np.log2(len(data)) ** 2 if len(data) > 0 else 0
        z_statistic = (longest_repeat - expected) / sqrt(variance) if variance > 0 else float('inf')  # Handle division by zero
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Longest Repeated Substring Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)