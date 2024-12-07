import numpy as np
from scipy.stats import chi2
from itertools import permutations
from concurrent.futures import ThreadPoolExecutor, as_completed

class Overlapping5PermutationTest:
    @staticmethod
    def _process_chunk(data_chunk, perm_lookup):
        """
        Helper function to process a chunk of data and count 5-permutations.
        """
        counts = np.zeros(120, dtype=int)
        k = len(data_chunk) // 5  # Number of 5-permutation blocks in this chunk

        for i in range(k):
            block = data_chunk[5 * i:5 * (i + 1)]  # Extract the 5-bit block
            sorted_indices = tuple(np.argsort(block))  # Get the permutation of the block
            perm_idx = perm_lookup[sorted_indices]  # Lookup the permutation index
            counts[perm_idx] += 1  # Increment the count for this permutation

        return counts

    @staticmethod
    def Overlapping5PermutationTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 

        if len(data) < 5:
            return -2, False  # Insufficient data, return failure result

        # Step 2: Convert binary string to a NumPy array for efficient processing
        try:
            data = np.fromiter(map(int, data), dtype=np.int8)
        except ValueError:
            return -2, False  # Return failure if the data is invalid

        k = len(data) // 5  # Number of 5-permutation blocks
        if k == 0:
            return -2, False  # Not enough data to create even one block

        # Step 3: Use NumPy to create a lookup table for all 120 5-permutations
        counts = np.zeros(120, dtype=int)  # 5! = 120 permutations
        perm_lookup = {perm: idx for idx, perm in enumerate(permutations(range(5)))}

        # Step 4: Divide data into chunks and process each chunk in parallel
        num_chunks = min(4, k)  # Adjust number of threads based on data length
        chunk_size = k // num_chunks * 5  # Ensure each chunk has a multiple of 5 elements

        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start = i * chunk_size
                end = start + chunk_size if i < num_chunks - 1 else len(data)
                futures.append(executor.submit(Overlapping5PermutationTest._process_chunk, data[start:end], perm_lookup))

            # Collect results from futures and merge counts
            for future in as_completed(futures):
                counts += future.result()

        # Step 5: Perform chi-square test
        expected_count = k / 120  # Each permutation is expected to occur equally
        chi_square = np.sum((counts - expected_count) ** 2 / expected_count)
        p_value = 1 - chi2.cdf(chi_square, 119)  # 119 degrees of freedom for 120 categories

        # Optional verbose output for debugging purposes
        if verbose:
            print(f"Overlapping 5-Permutation Test - Chi-square: {chi_square}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)