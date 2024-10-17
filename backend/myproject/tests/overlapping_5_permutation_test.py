import numpy as np
from scipy.stats import chi2
from itertools import permutations

class Overlapping5PermutationTest:
    @staticmethod
    def Overlapping5PermutationTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
       
        if len(data) < 5:
            return -1, False  # Insufficient data, return failure result

        # Step 2: Convert binary string to a NumPy array for efficient processing
        try:
            data = np.fromiter(map(int, data), dtype=np.int8)
        except ValueError:
            return -1, False  # Return failure if the data is invalid
        
        k = len(data) // 5  # Number of 5-permutation blocks
        if k == 0:
            return -1, False  # Not enough data to create even one block

        # Step 3: Use NumPy to create a lookup table for all 120 5-permutations
        counts = np.zeros(120, dtype=int)  # 5! = 120 permutations
        perm_lookup = {perm: idx for idx, perm in enumerate(permutations(range(5)))}

        # Step 4: Efficiently process the data in chunks of 5 bits
        for i in range(k):
            block = data[5*i:5*(i+1)]  # Extract the 5-bit block
            sorted_indices = tuple(np.argsort(block))  # Get the permutation of the block
            perm_idx = perm_lookup[sorted_indices]  # Lookup the permutation index
            counts[perm_idx] += 1  # Increment the count for this permutation

        # Step 5: Perform chi-square test
        expected_count = k / 120  # Each permutation is expected to occur equally
        chi_square = np.sum((counts - expected_count) ** 2 / expected_count)
        p_value = 1 - chi2.cdf(chi_square, 119)  # 119 degrees of freedom for 120 categories

        # Optional verbose output for debugging purposes
        if verbose:
            print(f"Overlapping 5-Permutation Test - Chi-square: {chi_square}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)
