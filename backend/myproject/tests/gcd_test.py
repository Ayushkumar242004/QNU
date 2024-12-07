import numpy as np
from scipy.stats import norm
from math import gcd
from concurrent.futures import ThreadPoolExecutor, as_completed

class MarsagliaTsangGCDTest:
    @staticmethod
    def calculate_gcd_pairs(data_array):
        """
        Calculate GCD of consecutive pairs in the data array.
        """
        return np.array([gcd(data_array[i], data_array[i + 1]) for i in range(len(data_array) - 1)])

    @staticmethod
    def MarsagliaTsangGCDTest(data, verbose=False):
        """
        Perform the Marsaglia-Tsang GCD Test on the provided binary data.
        """
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 2:
            return -2, False  # Return (-1, False) if insufficient data for GCD calculation
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)
        
        # Define the number of threads for parallel processing
        num_threads = 4  # Adjust this based on your CPU capabilities
        chunk_size = (n - 1) // num_threads + 1  # Size of each chunk

        gcd_results = []
        
        # Use ThreadPoolExecutor to parallelize the GCD calculation
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(0, n - 1, chunk_size):
                futures.append(executor.submit(MarsagliaTsangGCDTest.calculate_gcd_pairs, data_array[i:i + chunk_size + 1]))

            for future in as_completed(futures):
                gcd_results.append(future.result())
        
        # Flatten the list of results into a single array
        gcd_values = np.concatenate(gcd_results)

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