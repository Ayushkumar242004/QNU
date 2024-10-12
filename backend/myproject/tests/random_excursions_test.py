from math import isnan as isnan
from numpy import abs as abs
from numpy import append as append
from numpy import array as array
from numpy import clip as clip
from numpy import cumsum as cumsum
from numpy import ones as ones
from numpy import sqrt as sqrt
from numpy import sum as sum
from numpy import transpose as transpose
from numpy import where as where
from numpy import zeros as zeros
from scipy.special import erfc as erfc
from scipy.special import gammaincc as gammaincc

class RandomExcursions:


    @staticmethod
    def random_excursions_test(binary_data: str, target_state=-1):
        """
        The focus of this test is the total number of times that a particular state is visited (i.e., occurs) in a
        cumulative sum random walk. The purpose of this test is to detect deviations from the expected number
        of visits to various states in the random walk. This test is actually a series of eighteen tests (and
        conclusions), one test and conclusion for each of the states: -9, -8, …, -1 and +1, +2, …, +9.

        :param binary_data: a binary string
        :param target_state: The state to test
        :return: A tuple containing the p_value and result for the target state
        """

        length_of_binary_data = len(binary_data)
        length_of_binary_data = len(binary_data)
        # print('Length of binary string: ', length_of_binary_data)

        # Initialized k, m. n, pi and v_values
        if length_of_binary_data == 0:
            # Not enough data to run this test
            return None
            # return (0.00000, False, 'Error: Not enough data to run this test')

        sequence_x = zeros(length_of_binary_data)
        for i in range(len(binary_data)):
            if binary_data[i] == '0':
                sequence_x[i] = -1.0
            else:
                sequence_x[i] = 1.0

        cumulative_sum = cumsum(sequence_x)
        cumulative_sum = append(cumulative_sum, [0])
        cumulative_sum = append([0], cumulative_sum)

        x_values = array([-4, -3, -2, -1, 1, 2, 3, 4])
        index = list(x_values).index(target_state)

        position = where(cumulative_sum == 0)[0]
        cycles = []
        for pos in range(len(position) - 1):
            cycles.append(cumulative_sum[position[pos]:position[pos + 1] + 1])
        num_cycles = len(cycles)

        state_count = []
        for cycle in cycles:
            state_count.append(([len(where(cycle == target_state)[0])]))
        state_count = transpose(clip(state_count, 0, 5))

        su = []
        for cycle in range(6):
            su.append([(sct == cycle).sum() for sct in state_count])
        su = transpose(su)

        pi = ([([RandomExcursions.get_pi_value(uu, target_state) for uu in range(6)])])
        inner_term = num_cycles * array(pi)
        xObs = sum(1.0 * (array(su) - inner_term) ** 2 / inner_term, axis=1)
        chi_sq = xObs[0]
        p_value = gammaincc(2.5, xObs[0] / 2.0)
        result = p_value >= 0.01

        return chi_sq, p_value, result



    
    @staticmethod
    def get_frequency(li_data, target_state):
        """
        Helper method to get the frequency of a given state in li_data.
        :param li_data: List of data with cumulative sum counts
        :param target_state: The state to find in li_data
        :return: Frequency of the target state in li_data
        """
        for data in li_data:
            if data[0] == target_state:
                return data[1]
        return 0  # Return 0 if the target state is not found

    @staticmethod
    def get_pi_value(index, target_state):
        """
        Returns the expected probability value (pi) for a given index and target state.
        This is based on the target state for the random excursion variant test.
        :param index: The current index of the state
        :param target_state: The state being tested
        :return: The expected pi value
        """
        # Expected probabilities for target states
        pi_table = {
            -9: 0.00526, -8: 0.01053, -7: 0.01579, -6: 0.02105,
            -5: 0.02632, -4: 0.07895, -3: 0.15789, -2: 0.31579,
            -1: 0.5, 1: 0.5, 2: 0.31579, 3: 0.15789,
            4: 0.07895, 5: 0.02632, 6: 0.02105, 7: 0.01579,
            8: 0.01053, 9: 0.00526
        }
        return pi_table.get(target_state, 0)  # Return 0 if target_state is not in pi_table

    @staticmethod
    def variant_test(binary_data: str, target_state=1, verbose=False):
        """
        Performs the variant of the random excursions test for a specific target state.

        :param binary_data: a binary string
        :param target_state: The state to test
        :param verbose: Whether to print debug information
        :return: A tuple containing the chi_sq, p_value, and result for the target state
        """
        try:
            # Remove any invalid characters (anything other than 0 or 1)
            binary_data = ''.join([char for char in binary_data if char in '01'])

            # Check if binary_data is empty after sanitizing
            if not binary_data:
                raise ValueError("Input binary_data contains no valid binary characters (0 or 1)")

            length_of_binary_data = len(binary_data)
            int_data = zeros(length_of_binary_data)

            for count in range(length_of_binary_data):
                int_data[count] = int(binary_data[count])

            sum_int = (2 * int_data) - ones(len(int_data))
            cumulative_sum = cumsum(sum_int)

            li_data = []
            index = []
            for count in sorted(set(cumulative_sum)):
                if abs(count) <= 9:
                    index.append(count)
                    li_data.append([count, len(where(cumulative_sum == count)[0])])

            # Get frequency for state 0 and add 1
            j = RandomExcursions.get_frequency(li_data, 0) + 1

            p_values = []
            for count in (sorted(set(index))):
                if not count == 0:
                    den = sqrt(2 * j * (4 * abs(count) - 2))
                    p_values.append(erfc(abs(RandomExcursions.get_frequency(li_data, count) - j) / den))

            count = 0
            for data in li_data:
                if data[0] == 0:
                    li_data.remove(data)
                    index.remove(0)
                    break

            if verbose:
                print('Random Excursion Variant Test:')
                count = 0
                for item in p_values:
                    print('\t\t', repr(li_data[count][0]).rjust(4), '\t\t', li_data[count][1], '\t\t', repr(item).ljust(14), '\t\t', (item >= 0.01))
                    count += 1

            # Calculate chi_sq and p_value
            state_count = []
            for cycle in range(6):
                state_count.append([sct[1] for sct in li_data].count(cycle))  # Count occurrences of the cycle
            state_count = transpose([state_count])  # Transpose to get a column matrix

            num_cycles = len(li_data)
            pi = ([([RandomExcursions.get_pi_value(uu, target_state) for uu in range(6)])])
            inner_term = num_cycles * array(pi)
            xObs = sum(1.0 * (array(state_count) - inner_term) ** 2 / inner_term, axis=1)
            chi_sq = xObs[0]
            p_value = gammaincc(2.5, xObs[0] / 2.0)

            result = p_value >= 0.01

            return chi_sq, p_value, result
        except Exception as e:
            # In case of any error, return -1, False
            return -1, False
