import numpy as np
from scipy.stats import chi2  # Import chi2 for Chi-square distribution
from concurrent.futures import ThreadPoolExecutor, as_completed

class OPSOTest:
    @staticmethod
    def _compute_unique_pairs(data_chunk):
        """
        Helper function to compute unique pairs in a given data chunk.
        """
        unique_pairs = set()
        for i in range(len(data_chunk) - 1):
            pair = (data_chunk[i], data_chunk[i + 1])
            unique_pairs.add(pair)
        return unique_pairs

    @staticmethod
    def OPSOTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 2:
            return -1, False  # Return (-1, False) if insufficient data
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)
        
        # Define the number of chunks for parallel processing
        num_chunks = min(4, n - 1)  # Adjust number of threads based on data length
        chunk_size = (n - 1) // num_chunks
        
        # Split data into chunks and process in parallel
        unique_pairs = set()
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start = i * chunk_size
                end = start + chunk_size + 1 if i < num_chunks - 1 else n
                futures.append(executor.submit(OPSOTest._compute_unique_pairs, data_array[start:end]))

            # Collect results from futures and merge unique pairs
            for future in as_completed(futures):
                unique_pairs.update(future.result())

        # Compute observed unique pairs count
        observed = len(unique_pairs)
        expected = 4  # 2^2 = 4 possible binary pairs
        chi_square = ((observed - expected) ** 2) / expected
        
        # Chi-square test
        p_value = 1 - chi2.cdf(chi_square, 3)  # 4-1 = 3 degrees of freedom
        
        if verbose:
            print(f"OPSO Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)