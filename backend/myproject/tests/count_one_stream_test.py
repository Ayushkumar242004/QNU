import numpy as np
from scipy.stats import norm
from math import sqrt
from concurrent.futures import ThreadPoolExecutor, as_completed

class CountThe1sStreamTest:
    @staticmethod
    def CountThe1sStreamTest(data, verbose=False):
        # Step 1: Sanitize input data
        data = data.replace(',', '').strip()
        
        if not data:
            return None 

        # Split the data into chunks for parallel processing
        chunk_size = max(len(data) // 8, 1)  # Define a chunk size
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

        ones_count = 0
        total_count = 0

        # Parallel processing of each chunk
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(CountThe1sStreamTest.process_chunk, chunk) for chunk in chunks]
            for future in as_completed(futures):
                chunk_ones, chunk_total = future.result()
                ones_count += chunk_ones
                total_count += chunk_total

        if total_count == 0:
            return -1, False  # Handle case when no valid bits were processed

        # Calculate statistical values
        expected = total_count / 2
        variance = total_count / 4  # Variance for a binomial distribution (n/4 for p=0.5)
        
        if variance <= 0:
            return -1, False  # Variance must be positive

        z_statistic = (ones_count - expected) / sqrt(variance)  # Z-statistic calculation
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))  # Two-tailed p-value

        if verbose:
            print(f"Count-the-1s (Stream) Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)

    @staticmethod
    def process_chunk(chunk):
        ones_count = sum(1 for bit in chunk if bit == '1')
        total_count = sum(1 for bit in chunk if bit in ('0', '1'))
        return ones_count, total_count