import numpy as np
from scipy.stats import chi2  # Import chi2 for Chi-square distribution
from concurrent.futures import ThreadPoolExecutor, as_completed

class OQSOTest:
    @staticmethod
    def _compute_unique_quads(data_chunk):
        """
        Helper function to compute unique quadruples in a given data chunk.
        """
        unique_quads = set()
        for i in range(len(data_chunk) - 3):
            quad = (data_chunk[i], data_chunk[i + 1], data_chunk[i + 2], data_chunk[i + 3])
            unique_quads.add(quad)
        return unique_quads

    @staticmethod
    def OQSOTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 4:
            return -1, False  # Return (-1, False) if insufficient data
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)
        
        # Define the number of chunks for parallel processing
        num_chunks = min(4, (n - 3))  # Adjust number of threads based on data length
        chunk_size = (n - 3) // num_chunks
        
        # Split data into chunks and process in parallel
        unique_quads = set()
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start = i * chunk_size
                end = start + chunk_size + 3 if i < num_chunks - 1 else n
                futures.append(executor.submit(OQSOTest._compute_unique_quads, data_array[start:end]))

            # Collect results from futures and merge unique quadruples
            for future in as_completed(futures):
                unique_quads.update(future.result())

        # Compute observed unique quadruples count
        observed = len(unique_quads)
        expected = 16  # 2^4 = 16 possible binary quadruples
        chi_square = ((observed - expected) ** 2) / expected
        
        # Chi-square test
        p_value = 1 - chi2.cdf(chi_square, 15)  # 16-1 = 15 degrees of freedom
        
        if verbose:
            print(f"OQSO Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
