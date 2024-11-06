from math import floor, log, sqrt
from numpy import zeros
from scipy.special import erfc
from concurrent.futures import ThreadPoolExecutor, as_completed

class Universal:

    @staticmethod
    def process_block(block_data, i, vobs, init_bits):
        int_rep = int(block_data, 2)  # Convert block to integer representation
        if i < init_bits:
            vobs[int_rep] = i + 1
            return 0  # No cumsum update for initialization
        else:
            initial = vobs[int_rep]
            vobs[int_rep] = i + 1
            return log(i - initial + 1, 2)  # Calculate log for cumsum

    @staticmethod
    def statistical_test(binary_data: str, verbose=False):
        length_of_binary_data = len(binary_data)
        pattern_size = 5

        if length_of_binary_data == 0:
            return (0.00000, False, 'Error: Not enough data to run this test')

        # Determine pattern size based on length of binary data
        thresholds = [387840, 904960, 2068480, 4654080, 10342400, 22753280, 49643520, 107560960, 231669760, 496435200]
        for i, threshold in enumerate(thresholds, start=6):
            if length_of_binary_data >= threshold:
                pattern_size = i

        if 5 < pattern_size < 16:
            ones = "1" * pattern_size
            num_ints = int(ones, 2)
            vobs = zeros(num_ints + 1)

            num_blocks = floor(length_of_binary_data / pattern_size)
            init_bits = 10 * pow(2, pattern_size)
            test_bits = num_blocks - init_bits

            c = 0.7 - 0.8 / pattern_size + (4 + 32 / pattern_size) * pow(test_bits, -3 / pattern_size) / 15
            variance = [0, 0, 0, 0, 0, 0, 2.954, 3.125, 3.238, 3.311, 3.356, 3.384, 3.401, 3.410, 3.416, 3.419, 3.421]
            expected = [0, 0, 0, 0, 0, 0, 5.2177052, 6.1962507, 7.1836656, 8.1764248, 9.1723243,
                        10.170032, 11.168765, 12.168070, 13.167693, 14.167488, 15.167379]
            sigma = c * sqrt(variance[pattern_size] / test_bits)

            cumsum = 0.0
            blocks = [(binary_data[i * pattern_size:(i + 1) * pattern_size], i) for i in range(num_blocks)]

            with ThreadPoolExecutor() as executor:
                futures = {executor.submit(Universal.process_block, block_data, i, vobs, init_bits): i for block_data, i in blocks}
                for future in as_completed(futures):
                    cumsum += future.result()  # Add results to cumsum

            phi = float(cumsum / test_bits)
            stat = abs(phi - expected[pattern_size]) / (float(sqrt(2)) * sigma)

            # Compute for P-Value
            p_value = erfc(stat)

            if verbose:
                print('Maurer\'s Universal Statistical Test')
                print('\tP-Value:\t\t\t\t', p_value)

            return (p_value, (p_value >= 0.01))
        else:
            return (-1.0, False)