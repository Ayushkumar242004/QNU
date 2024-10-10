import numpy as np
from scipy.stats import chi2
from itertools import permutations

class Overlapping5PermutationTest:
    @staticmethod
    def Overlapping5PermutationTest(data, verbose=False):
        # Sanitize input by removing non-binary characters (e.g., commas)
        data = data.replace(',', '').strip()

        # Ensure that the data length is at least 5
        if len(data) < 5:
            return -1, False  # Insufficient data, return failure result

        # Convert the binary string to a list of integers
        try:
            data = [int(bit) for bit in data]
        except ValueError:
            return -1, False  # Return failure if data cannot be parsed as integers

        k = len(data) // 5  # Number of 5-permutation blocks
        if k == 0:
            return -1, False  # Return failure if no valid 5-bit blocks

        counts = np.zeros(120)  # 5! = 120 permutations

        # Create a lookup for all possible 5-permutations
        perm_lookup = {perm: idx for idx, perm in enumerate(permutations(range(5)))}

        # Loop through the data in 5-bit blocks
        for i in range(k):
            # Get the 5-bit block and find its permutation index
            perm = tuple(np.argsort(data[5*i:5*(i+1)]))
            perm_idx = perm_lookup[perm]  # Map permutation to index
            counts[perm_idx] += 1

        expected_count = k / 120  # Each permutation is expected to occur equally
        chi_square = np.sum((counts - expected_count) ** 2 / expected_count)
        p_value = 1 - chi2.cdf(chi_square, 119)

        if verbose:
            print(f"Overlapping 5-Permutation Test - Chi-square: {chi_square}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)
