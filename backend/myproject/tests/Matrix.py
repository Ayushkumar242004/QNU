from math import exp, floor
from numpy import zeros
from concurrent.futures import ThreadPoolExecutor, as_completed
from .BinaryMatrix import BinaryMatrix as bm

class Matrix:

    @staticmethod
    def _compute_block_rank(block_data, shape, rows_in_matrix, columns_in_matrix):
        """
        Helper function to compute the rank of a single block of binary data.

        Parameters:
            block_data (str): A binary sequence representing the block.
            shape (tuple): Shape of the matrix to be created.
            rows_in_matrix (int): Number of rows in the matrix.
            columns_in_matrix (int): Number of columns in the matrix.

        Returns:
            int: The rank of the matrix formed by the block data.
        """
        # Convert the block data to a matrix
        block = zeros(len(block_data))
        for count in range(len(block_data)):
            if block_data[count] == '1':
                block[count] = 1.0
        matrix = block.reshape(shape)

        # Compute the rank
        ranker = bm(matrix, rows_in_matrix, columns_in_matrix)
        return ranker.compute_rank()

    @staticmethod
    def binary_matrix_rank_text(binary_data: str, verbose=False, rows_in_matrix=32, columns_in_matrix=32):
        """
        Perform the Binary Matrix Rank Test on a binary sequence to check for randomness.

        Parameters:
            binary_data (str): A binary sequence (0s and 1s).
            verbose (bool): If True, prints detailed debug information.
            rows_in_matrix (int): Number of rows in each matrix (default is 32).
            columns_in_matrix (int): Number of columns in each matrix (default is 32).

        Returns:
            tuple: (p_value, bool) where bool indicates if the sequence is random.
        """
        length_of_binary_data = len(binary_data)
        if length_of_binary_data == 0:
            return (-2, False, 'Error: Not enough data to run this test')

        shape = (rows_in_matrix, columns_in_matrix)
        block_size = rows_in_matrix * columns_in_matrix
        number_of_blocks = floor(length_of_binary_data / block_size)
        max_ranks = [0, 0, 0]

        if number_of_blocks > 0:
            block_data_segments = [
                binary_data[i * block_size: (i + 1) * block_size]
                for i in range(number_of_blocks)
            ]

            with ThreadPoolExecutor() as executor:
                futures = {
                    executor.submit(Matrix._compute_block_rank, block_data, shape, rows_in_matrix, columns_in_matrix): block_data
                    for block_data in block_data_segments
                }

                for future in as_completed(futures):
                    try:
                        rank = future.result()
                        if rank == rows_in_matrix:
                            max_ranks[0] += 1
                        elif rank == (rows_in_matrix - 1):
                            max_ranks[1] += 1
                        else:
                            max_ranks[2] += 1
                    except Exception as e:
                        print(f"Error computing rank for block: {e}")

            # Probabilities for full rank, rank-1, and lower
            pi = [1.0, 0.0, 0.0]
            for x in range(1, 50):
                pi[0] *= 1 - (1.0 / (2 ** x))
            pi[1] = 2 * pi[0]
            pi[2] = 1 - pi[0] - pi[1]

            # Calculate chi-squared statistic
            xObs = sum(pow((max_ranks[i] - pi[i] * number_of_blocks), 2.0) / (pi[i] * number_of_blocks) for i in range(len(pi)))

            # Calculate p-value
            p_value = exp(-xObs / 2)

            if verbose:
                print('Binary Matrix Rank Test:')
                print('\tP-Value:\t\t\t', p_value)

            return (p_value, (p_value >= 0.01))
        else:
            return (-2.0, False)