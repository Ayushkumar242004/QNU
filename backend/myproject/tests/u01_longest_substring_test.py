from math import sqrt
from scipy.stats import norm
import numpy as np

class TestU01LongestRepeatedSubstringTest:
    @staticmethod
    def TestU01LongestRepeatedSubstringTest(data, verbose=False):
        longest_repeat = max([len(sub) for sub in set(data) if data.count(sub) > 1], default=0)
        expected = np.log2(len(data))
        variance = np.log2(len(data)) ** 2
        z_statistic = (longest_repeat - expected) / sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Longest Repeated Substring Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
