from math import fabs as fabs
from math import floor as floor
from math import sqrt as sqrt
from scipy.special import erfc as erfc
from scipy.special import gammaincc as gammaincc
from numpy import zeros as zeros

class RunTest:

    @staticmethod
    def run_test(binary_data: str, verbose=False):
        """
        The focus of this test is the total number of runs in the sequence,
        where a run is an uninterrupted sequence of identical bits.
        A run of length k consists of exactly k identical bits and is bounded before
        and after with a bit of the opposite value. The purpose of the runs test is to
        determine whether the number of runs of ones and zeros of various lengths is as
        expected for a random sequence. In particular, this test determines whether the
        oscillation between such zeros and ones is too fast or too slow.

        :param      binary_data:        The sequence of bits being tested
        :param      verbose:            True to display the debug message, False to turn off debug message
        :return:    (p_value, bool)     A tuple that contains the p_value and result of the frequency test (True or False)
        """
        vObs = 0
        length_of_binary_data = len(binary_data)

        # Predefined tau = 2 / sqrt(n)
        tau = 2 / sqrt(length_of_binary_data)

        # Step 1 - Compute the proportion π of ones in the input sequence
        one_count = binary_data.count('1')
        pi = one_count / length_of_binary_data

        # Step 2 - Check if |π - 0.5| >= tau
        if abs(pi - 0.5) >= tau:
            # The test should not proceed because of a failure to pass the pre-test
            return (0.0000, False)

        # Step 3 - Compute vObs (number of runs)
        for item in range(1, length_of_binary_data):
            if binary_data[item] != binary_data[item - 1]:
                vObs += 1
        vObs += 1

        try:
            # Step 4 - Compute p_value using the erfc function
            p_value = erfc(abs(vObs - (2 * length_of_binary_data * pi * (1 - pi))) /
                        (2 * sqrt(2 * length_of_binary_data) * pi * (1 - pi)))

        except ZeroDivisionError:
            # Return -1 in case of a division by zero error
            return (-1, False)

        if verbose:
            print('Run Test DEBUG BEGIN:')
            print('\tP-Value:\t\t\t\t\t\t', p_value)

        # Return the p_value and whether the test passed (p_value > 0.01)
        return (p_value, (p_value > 0.01))

    @staticmethod
    def longest_one_block_test(binary_data: str, verbose=False):
        """
        The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to determine
        whether the length of the longest run of ones within the tested sequence is consistent with the length of the
        longest run of ones that would be expected in a random sequence. Note that an irregularity in the expected
        length of the longest run of ones implies that there is also an irregularity in the expected length of the 
        longest run of zeroes. Therefore, only a test for ones is necessary.

        :param      binary_data:        The sequence of bits being tested
        :param      verbose             True to display the debug message, False to turn off debug message
        :return:    (p_value, bool)     A tuple which contains the p_value and result of frequency_test(True or False)
        """
        length_of_binary_data = len(binary_data)

        # Initialize k, m, v_values, and pi_values
        if length_of_binary_data < 128:
            return (-1, False, 'Error: Not enough data to run this test')
        elif length_of_binary_data < 6272:
            k = 3
            m = 8
            v_values = [1, 2, 3, 4]
            pi_values = [0.21484375, 0.3671875, 0.23046875, 0.1875]
        elif length_of_binary_data < 750000:
            k = 5
            m = 128
            v_values = [4, 5, 6, 7, 8, 9]
            pi_values = [0.1174035788, 0.242955959, 0.249363483, 0.17517706, 0.102701071, 0.112398847]
        else:
            # If length_of_bit_string > 750000
            k = 6
            m = 10000
            v_values = [10, 11, 12, 13, 14, 15, 16]
            pi_values = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]

        number_of_blocks = floor(length_of_binary_data / m)
        block_start = 0
        block_end = m
        xObs = 0
        frequencies = zeros(k + 1)

        for count in range(number_of_blocks):
            block_data = binary_data[block_start:block_end]
            max_run_count = 0
            run_count = 0

            # Count the number of ones in the block
            for bit in block_data:
                if bit == '1':
                    run_count += 1
                    max_run_count = max(max_run_count, run_count)
                else:
                    max_run_count = max(max_run_count, run_count)
                    run_count = 0

            max_run_count = max(max_run_count, run_count)

            if max_run_count < v_values[0]:
                frequencies[0] += 1
            for j in range(k):
                if max_run_count == v_values[j]:
                    frequencies[j] += 1
            if max_run_count > v_values[k - 1]:
                frequencies[k] += 1

            block_start += m
            block_end += m

        # Compute xObs
        for count in range(len(frequencies)):
            xObs += pow((frequencies[count] - (number_of_blocks * pi_values[count])), 2.0) / (
                    number_of_blocks * pi_values[count])

        p_value = gammaincc(float(k / 2), float(xObs / 2))

        if verbose:
            print('Run Test (Longest Run of Ones in a Block) :')
            print('\tP-Value:\t\t\t\t\t\t', p_value)

        # Consistent return values
        if length_of_binary_data < 128:
            return (-1, False, 'Error: Not enough data to run this test')
        
        return (p_value, (p_value > 0.01), None)
