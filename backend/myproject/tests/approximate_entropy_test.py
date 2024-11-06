from math import log as log
from numpy import zeros as zeros
from scipy.special import gammaincc as gammaincc
from concurrent.futures import ThreadPoolExecutor, as_completed

class ApproximateEntropy:

    @staticmethod
    def _calculate_frequencies(binary_data_chunk: str, pattern_length: int):
        """
        Helper function to calculate the frequency of patterns in a binary data chunk.
        """
        # Initialize frequency counts
        max_pattern_length = pattern_length + 1
        vobs_01 = zeros(2 ** pattern_length)
        vobs_02 = zeros(2 ** max_pattern_length)

        # Calculate frequency of overlapping m-bit and (m+1)-bit patterns
        for i in range(len(binary_data_chunk) - pattern_length):
            vobs_01[int(binary_data_chunk[i:i + pattern_length], 2)] += 1
            vobs_02[int(binary_data_chunk[i:i + pattern_length + 1], 2)] += 1

        return vobs_01, vobs_02

    @staticmethod
    def approximate_entropy_test(binary_data: str, verbose=False, pattern_length=10):
        """
        Approximate entropy test to compare the frequency of overlapping patterns.
        """
        binary_data = ''.join(filter(lambda x: x in '01', binary_data))

        length_of_binary_data = len(binary_data)
        if length_of_binary_data < pattern_length:
            if verbose:
                print(f"Binary data is too short: {length_of_binary_data} < {pattern_length}")
            return -1, False

        # Augment the binary data to create overlapping patterns
        binary_data += binary_data[:pattern_length + 1]

        # Split the data into chunks for parallel processing
        chunk_size = length_of_binary_data // 4  # Adjust the number of chunks as needed
        chunks = [binary_data[i:i + chunk_size + pattern_length + 1] for i in range(0, length_of_binary_data, chunk_size)]

        # Initialize results storage
        vobs_01_total = zeros(2 ** pattern_length)
        vobs_02_total = zeros(2 ** (pattern_length + 1))

        # Use ThreadPoolExecutor to calculate frequencies in parallel
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(ApproximateEntropy._calculate_frequencies, chunk, pattern_length): chunk for chunk in chunks}
            for future in as_completed(futures):
                vobs_01, vobs_02 = future.result()
                vobs_01_total += vobs_01
                vobs_02_total += vobs_02

        # Calculate the test statistics and p-values
        vobs = [vobs_01_total, vobs_02_total]

        sums = zeros(2)
        for i in range(2):
            for j in range(len(vobs[i])):
                if vobs[i][j] > 0:
                    sums[i] += vobs[i][j] * log(vobs[i][j] / length_of_binary_data)
        sums /= length_of_binary_data
        ape = sums[0] - sums[1]

        xObs = 2.0 * length_of_binary_data * (log(2) - ape)
        p_value = gammaincc(2 ** (pattern_length - 1), xObs / 2.0)

        if verbose:
            print('Approximate Entropy Test: ')
            print('\tP-Value:\t\t\t\t\t', p_value)

        return p_value, (p_value >= 0.01)
