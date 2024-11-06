from scipy.stats import chi2  # Import chi2 for the chi-square test
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

class DNATest:
    @staticmethod
    def DNATest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Check for empty input data
        if len(data) == 0:
            return -1, False
        
        if not isinstance(data, str) or len(data) < 10:
            return -1, False
        
        n = len(data)
        subsequence_count = defaultdict(int)  # Dictionary to count occurrences of each subsequence

        # Split data into chunks for parallel processing
        num_chunks = min(8, (n - 10) // 10 + 1)  # Adjust based on your needs
        chunk_size = (n - 10) // num_chunks + 1
        
        def process_chunk(chunk_start, chunk_end):
            local_count = defaultdict(int)
            for i in range(chunk_start, chunk_end):
                subseq = data[i:i + 10]  # Get the substring of length 10
                local_count[subseq] += 1
            return local_count

        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start_index = i * chunk_size
                end_index = min(start_index + chunk_size, n - 9)  # Ensure not to go out of bounds
                if start_index < end_index:
                    futures.append(executor.submit(process_chunk, start_index, end_index))

            # Aggregate results from all threads
            for future in as_completed(futures):
                local_count = future.result()
                for subseq, count in local_count.items():
                    subsequence_count[subseq] += count

        observed = len(subsequence_count)  # Count of unique subsequences
        expected = 1024  # 2^10 = 1024 possible binary subsequences
        chi_square = ((observed - expected) ** 2) / expected
        
        # Calculate the p-value
        p_value = 1 - chi2.cdf(chi_square, 1023)  # 1024-1 = 1023 degrees of freedom
        
        if verbose:
            print(f"DNA Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)  # Return p-value and pass/fail result