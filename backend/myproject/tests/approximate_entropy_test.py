from math import log as log
from numpy import zeros as zeros
from scipy.special import gammaincc as gammaincc

class ApproximateEntropy:

    @staticmethod
    def approximate_entropy_test(binary_data: str, verbose=False, pattern_length=10):
        """
        from the NIST documentation http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf

        As with the Serial test of Section 2.11, the focus of this test is the frequency of all possible
        overlapping m-bit patterns across the entire sequence. The purpose of the test is to compare
        the frequency of overlapping blocks of two consecutive/adjacent lengths (m and m+1) against the
        expected result for a random sequence.

        :param      binary_data:        a binary string
        :param      verbose             True to display the debug message, False to turn off debug message
        :param      pattern_length:     the length of the pattern (m)
        :return:    ((p_value1, bool), (p_value2, bool)) A tuple which contain the p_value and result of the test (True or False)
        """
        # Clean the binary_data by removing invalid characters (anything other than '0' or '1')
        binary_data = ''.join(filter(lambda x: x in '01', binary_data))

        # Check if the cleaned binary data has enough length for the test
        length_of_binary_data = len(binary_data)
        if length_of_binary_data < pattern_length:
            if verbose:
                print(f"Binary data is too short: {length_of_binary_data} < {pattern_length}")
            return -1, False

        # Augment the n-bit sequence to create n overlapping m-bit sequences
        binary_data += binary_data[:pattern_length + 1]

        # Get the maximum length one patterns for m and m+1
        max_pattern = ''.join('1' for _ in range(pattern_length + 2))

        # Keep track of each pattern's frequency (how often it appears)
        vobs_01 = zeros(int(max_pattern[:pattern_length], 2) + 1)
        vobs_02 = zeros(int(max_pattern[:pattern_length + 1], 2) + 1)

        for i in range(length_of_binary_data):
            try:
                # Work out what pattern is observed and increment its frequency count
                vobs_01[int(binary_data[i:i + pattern_length], 2)] += 1
                vobs_02[int(binary_data[i:i + pattern_length + 1], 2)] += 1
            except ValueError:
                continue  # Skip invalid binary slices

        # Calculate the test statistics and p-values
        vobs = [vobs_01, vobs_02]

        sums = zeros(2)
        for i in range(2):
            for j in range(len(vobs[i])):
                if vobs[i][j] > 0:
                    sums[i] += vobs[i][j] * log(vobs[i][j] / length_of_binary_data)
        sums /= length_of_binary_data
        ape = sums[0] - sums[1]

        xObs = 2.0 * length_of_binary_data * (log(2) - ape)

        # Compute the p-value using gammaincc
        p_value = gammaincc(pow(2, pattern_length - 1), xObs / 2.0)

        if verbose:
            print('Approximate Entropy Test: ')
            print('\tP-Value:\t\t\t\t\t', p_value)

        # Return the p-value and a boolean indicating whether the test passed (p_value >= 0.01)
        return p_value, (p_value >= 0.01)
