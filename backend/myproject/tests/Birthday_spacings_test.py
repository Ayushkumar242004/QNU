import numpy as np
from scipy.stats import chi2
from concurrent.futures import ThreadPoolExecutor, as_completed

class BirthdaySpacingsTest:
    @staticmethod
    def BirthdaySpacingsTest(data, t=512, verbose=False):
        if not data:
            return -2, False
        # Return -1, False if no data or insufficient data
        if len(data) < 3:
            return -2, False
        
        
        try:
            # Convert binary string data into an array of integers
            data = [int(bit) for bit in data]  # Convert each character to integer
            mod_data = np.array(data) % t  # Convert to numpy array and apply modulus

            # Split mod_data into chunks for parallel sorting
            num_chunks = min(8, len(mod_data))  # Use 8 or fewer threads based on data size
            chunk_size = len(mod_data) // num_chunks
            sorted_chunks = []

            # Parallel sorting of each chunk
            with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(np.sort, mod_data[i * chunk_size:(i + 1) * chunk_size])
                    for i in range(num_chunks)
                ]
                for future in as_completed(futures):
                    sorted_chunks.append(future.result())

            # Merge sorted chunks into one sorted array
            sorted_mod_data = np.concatenate(sorted_chunks)
            sorted_mod_data.sort()  # Final sort after concatenation for proper order

            # Calculate spacings from sorted data
            spacings = np.diff(sorted_mod_data)
            k = len(spacings)

            if k == 0 or np.mean(spacings) == 0:
                return -5, False  # Handle cases where spacings are empty or mean is zero

            # Chi-square calculation based on spacings
            chi_square = (np.var(spacings) / np.mean(spacings)) * (k - 1)
            p_value = 1 - chi2.cdf(chi_square, k - 1)

            if verbose:
                print(f"Birthday Spacings Test - Chi-square: {chi_square}, p-value: {p_value}")

            return p_value, (p_value >= 0.01)  # Return p-value and pass/fail result

        except Exception as e:
            # Catch any other exceptions and return -1, False
            print(f"Error: {e}")
            return -4, False