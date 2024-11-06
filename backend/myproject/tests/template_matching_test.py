from math import floor as floor
from numpy import array as array, exp as exp, zeros as zeros
from scipy.special import gammaincc as gammaincc, hyp1f1 as hyp1f1
from concurrent.futures import ThreadPoolExecutor, as_completed

class TemplateMatching:

    @staticmethod
    def non_overlapping_test(binary_data: str, verbose=False, template_pattern='000000001', block=8):
        length_of_binary = len(binary_data)
        if length_of_binary == 0:
            return (0.00000, False, 'Error: Not enough data to run this test')

        pattern_size = len(template_pattern)
        block_size = floor(length_of_binary / block)
        pattern_counts = zeros(block)

        def process_block(count):
            block_start = count * block_size
            block_end = block_start + block_size
            block_data = binary_data[block_start:block_end]
            inner_count = 0
            pattern_count = 0
            while inner_count < block_size:
                sub_block = block_data[inner_count:inner_count + pattern_size]
                if sub_block == template_pattern:
                    pattern_count += 1
                    inner_count += pattern_size
                else:
                    inner_count += 1
            return pattern_count

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_block, count) for count in range(block)]
            for i, future in enumerate(as_completed(futures)):
                pattern_counts[i] = future.result()

        mean = (block_size - pattern_size + 1) / pow(2, pattern_size)
        variance = block_size * ((1 / pow(2, pattern_size)) - (((2 * pattern_size) - 1) / (pow(2, pattern_size * 2))))
        xObs = sum((pattern_counts - mean) ** 2 / variance)

        p_value = gammaincc((block / 2), (xObs / 2))

        if verbose:
            print('Non-Overlapping Template Test DEBUG BEGIN:')
            print('\tP-Value:\t\t\t\t', p_value)

        return (p_value, (p_value >= 0.01))

    @staticmethod
    def overlapping_patterns(binary_data: str, verbose=False, pattern_size=8, block_size=8):
        length_of_binary_data = len(binary_data)
        if length_of_binary_data == 0:
            return (0.00000, False, 'Error: Not enough data to run this test')

        pattern = '1' * pattern_size
        number_of_block = floor(length_of_binary_data / block_size)
        lambda_val = float(block_size - pattern_size + 1) / pow(2, pattern_size)
        eta = lambda_val / 2.0
        pi = [TemplateMatching.get_prob(i, eta) for i in range(5)]
        pi.append(1.0 - float(array(pi).sum()))

        pattern_counts = zeros(6)

        def count_patterns(i):
            block_start = i * block_size
            block_end = block_start + block_size
            block_data = binary_data[block_start:block_end]
            pattern_count = 0
            j = 0
            while j < block_size:
                sub_block = block_data[j:j + pattern_size]
                if sub_block == pattern:
                    pattern_count += 1
                j += 1
            return min(pattern_count, 5)

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(count_patterns, i) for i in range(number_of_block)]
            for future in as_completed(futures):
                pattern_counts[future.result()] += 1

        xObs = sum(pow(pattern_counts[i] - number_of_block * pi[i], 2) / (number_of_block * pi[i]) for i in range(6))
        p_value = gammaincc(5.0 / 2.0, xObs / 2.0)

        if verbose:
            print('Overlapping Template Test :')
            print('\tP-Value:\t\t\t\t', p_value)

        return (p_value, (p_value >= 0.01))

    @staticmethod
    def get_prob(u, x):
        out = 1.0 * exp(-x)
        if u != 0:
            out = 1.0 * x * exp(2 * -x) * (2 ** -u) * hyp1f1(u + 1, 2, x)
        return out

