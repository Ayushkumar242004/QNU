import numpy as np
from scipy.stats import norm
from concurrent.futures import ThreadPoolExecutor, as_completed
from math import ceil, floor

class CumulativeSums:

    @staticmethod
    def cumulative_sums_test(binary_data: str, mode=0, verbose=False):
        """
        Cumulative Sums Test for randomness.

        :param binary_data: A binary string.
        :param mode: A switch for applying the test either forward (mode=0) or backward (mode=1).
        :param verbose: True to display debug messages, False to turn off debug messages.
        :return: (p_value, bool) A tuple containing the p_value and the test result (True or False).
        """
        try:

            length_of_binary_data = len(binary_data)
            if(length_of_binary_data == 0):
                return None 
            counts = np.zeros(length_of_binary_data)

            # Determine whether forward or backward data
            if mode != 0:
                binary_data = binary_data[::-1]

            # Split binary data into chunks for parallel processing
            num_chunks = min(8, ceil(length_of_binary_data / 1000))  # Adjust based on your needs

            # Handle the case where num_chunks is 0
            if num_chunks == 0:
                if verbose:
                    print("Error: num_chunks is 0, binary_data is too short.")
                return -4, False

            chunk_size = ceil(length_of_binary_data / num_chunks)

            with ThreadPoolExecutor() as executor:
                futures = []
                for i in range(num_chunks):
                    start_index = i * chunk_size
                    end_index = min(start_index + chunk_size, length_of_binary_data)
                    futures.append(
                        executor.submit(
                            CumulativeSums.process_chunk, binary_data[start_index:end_index], i == 0
                        )
                    )

                for i, future in enumerate(as_completed(futures)):
                    result = future.result()
                    if isinstance(result, tuple) and result == (-4, False):
                        return result

                    # Update the corresponding section of the counts array
                    start_index = i * chunk_size
                    end_index = min(start_index + chunk_size, length_of_binary_data)
                    counts[start_index:end_index] += result

            # Compute the test statistic z = max1≤k≤n |Sk|, where Sk is the partial sums
            abs_max = max(abs(counts))

            start = int(floor(0.25 * floor(-length_of_binary_data / abs_max) + 1))
            end = int(floor(0.25 * floor(length_of_binary_data / abs_max) - 1))

            terms_one = []
            for k in range(start, end + 1):
                sub = norm.cdf((4 * k - 1) * abs_max / np.sqrt(length_of_binary_data))
                terms_one.append(norm.cdf((4 * k + 1) * abs_max / np.sqrt(length_of_binary_data)) - sub)

            start = int(floor(0.25 * floor(-length_of_binary_data / abs_max - 3)))
            end = int(floor(0.25 * floor(length_of_binary_data / abs_max) - 1))

            terms_two = []
            for k in range(start, end + 1):
                sub = norm.cdf((4 * k + 1) * abs_max / np.sqrt(length_of_binary_data))
                terms_two.append(norm.cdf((4 * k + 3) * abs_max / np.sqrt(length_of_binary_data)) - sub)

            p_value = 1.0 - np.sum(np.array(terms_one))
            p_value += np.sum(np.array(terms_two))

            if verbose:
                print('Cumulative Sums Test: ')
                print('\tP-Value:\t\t\t', p_value)

            return (p_value, (p_value >= 0.01))
        
        except Exception as e:
            if verbose:
                print(f"Error in cumulative_sums_test: {e}")
            return -4, False

    @staticmethod
    def process_chunk(chunk, is_first_chunk):
        """Process a chunk of binary data to calculate cumulative sums."""
        try:
            counts = np.zeros(len(chunk))
            counter = 0

            for char in chunk:
                sub = 1 if char == '1' else -1
                if counter > 0:
                    counts[counter] = counts[counter - 1] + sub
                else:
                    counts[counter] = sub
                counter += 1

            # Adjust for the first chunk to include the cumulative sum of the last element
            if not is_first_chunk and len(chunk) > 0:
                counts[0] += counts[-1]

            return counts
        except Exception as e:
            print(f"Error in process_chunk: {e}")
            return -4, False
