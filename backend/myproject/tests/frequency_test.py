from math import fabs, floor, sqrt
from scipy.special import erfc, gammaincc
from concurrent.futures import ThreadPoolExecutor, as_completed

class FrequencyTest:

    @staticmethod
    def monobit_test(binary_data: str, verbose=False):
        """
        Monobit test for randomness.
        """
        if len(binary_data) == 0:
            return (0.00000, False, 'Error: Not enough data to run this test')

        length_of_bit_string = len(binary_data)

        # Split data into chunks for parallel processing
        num_chunks = min(8, length_of_bit_string // 10) if length_of_bit_string >= 10 else 1  # Number of threads
        chunk_size = length_of_bit_string // num_chunks

        def process_chunk(start_index, end_index):
            count = 0
            for bit in binary_data[start_index:end_index]:
                if bit == '0':
                    count -= 1
                elif bit == '1':
                    count += 1
            return count

        total_count = 0
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start_index = i * chunk_size
                end_index = start_index + chunk_size if i < num_chunks - 1 else length_of_bit_string
                futures.append(executor.submit(process_chunk, start_index, end_index))

            # Aggregate results from all threads
            for future in as_completed(futures):
                total_count += future.result()

        # Compute the test statistic
        sObs = total_count / sqrt(length_of_bit_string)

        # Compute p-Value
        p_value = erfc(fabs(sObs) / sqrt(2))

        if verbose:
            print('Frequency Test (Monobit Test):')
            print('\tP-Value:\t\t\t', p_value)

        return (p_value, (p_value >= 0.01))

    @staticmethod
    def block_frequency(binary_data: str, block_size=128, verbose=False):
        """
        Block frequency test for randomness.
        """
        if not binary_data:
            return None, None 

        length_of_bit_string = len(binary_data)

        if block_size <= 0:
            return -1, False  # Ensure we always return some p_value

        if length_of_bit_string < block_size:
            return -1, False  # Return (-1, False) if not enough data

        number_of_blocks = floor(length_of_bit_string / block_size)

        if number_of_blocks <= 1:
            return -1, False

        def process_block(start_index):
            block_data = binary_data[start_index:start_index + block_size]
            one_count = block_data.count('1')
            pi = one_count / block_size
            return (pi - 0.5) ** 2

        proportion_sum = 0.0
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(number_of_blocks):
                start_index = i * block_size
                futures.append(executor.submit(process_block, start_index))

            # Aggregate results from all threads
            for future in as_completed(futures):
                proportion_sum += future.result()

        # Compute 4M Σ(πi -½)^2.
        result = 4.0 * block_size * proportion_sum

        # Compute P-Value
        p_value = gammaincc(number_of_blocks / 2, result / 2)

        if verbose:
            print('Frequency Test (Block Frequency Test) DEBUG BEGIN:')
            print('\tP-Value:\t\t\t', p_value)

        return p_value, (p_value >= 0.01)