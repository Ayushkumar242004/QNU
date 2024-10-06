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
    def variant_test(binary_data: str, target_state=1, verbose=False):
        """
        Performs the variant of the random excursions test for a specific target state.

        :param binary_data: a binary string
        :param target_state: The state to test
        :param verbose: Whether to print debug information
        :return: A tuple containing the chi_sq, p_value, and result for the target state
        """
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

        j = RandomExcursions.get_frequency(li_data, 0) + 1

        p_values = []
        for count in (sorted(set(index))):
            if not count == 0:
                den = sqrt(2 * j * (4 * abs(count) - 2))
                p_values.append(erfc(abs(RandomExcursions.get_frequency(li_data, count) - j) / den))

        count = 0
        # Remove 0 from li_data so the number of elements will be equal to p_values
        for data in li_data:
            if data[0] == 0:
                li_data.remove(data)
                index.remove(0)
                break
            count += 1

        if verbose:
            print('Random Excursion Variant Test:')
            # print("\tLength of input:\t", length_of_binary_data)
            # print('\tValue of j:\t\t', j)
            print('\tP-Values:')
            # print('\t\t STATE \t\t COUNTS \t\t P-Value \t\t Conclusion')
            count = 0
            for item in p_values:
                print('\t\t', repr(li_data[count][0]).rjust(4), '\t\t', li_data[count][1], '\t\t', repr(item).ljust(14), '\t\t', (item >= 0.01))
                count += 1
            # print('DEBUG END.')

        states = []
        for item in index:
            if item < 0:
                states.append(str(int(item)))  # Convert negative floats to integers
            else:
                states.append('+' + str(int(item)))  # Convert positive floats to integers

        result = []
        count = 0
        for item in p_values:
            if int(states[count]) == target_state:
                result.append((states[count], li_data[count][0], li_data[count][1], item, (item >= 0.01)))
                break
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

        return chi_sq, p_value, result



    @staticmethod
    def get_pi_value(k, x):
        """
        This method is used by the random_excursions method to get expected probabilities
        """
        if k == 0:
            out = 1 - 1.0 / (2 * abs(x))
        elif k >= 5:
            out = (1.0 / (2 * abs(x))) * (1 - 1.0 / (2 * abs(x))) ** 4
        else:
            out = (1.0 / (4 * x * x)) * (1 - 1.0 / (2 * abs(x))) ** (k - 1)
        return out

    @staticmethod
    def get_frequency(list_data, trigger):
        """
        This method is used by the random_excursions_variant method to get frequencies
        """
        frequency = 0
        for (x, y) in list_data:
            if x == trigger:
                frequency = y
        return frequency