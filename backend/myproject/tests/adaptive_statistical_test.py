import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class AdaptiveStatisticalTest:

    @staticmethod
    def generate_random_deviation(sequence_length):
        """Generate a random sequence and calculate its max deviation."""
        random_sequence = np.random.choice([0, 1], size=sequence_length)
        cumulative_sum_random = np.cumsum(random_sequence) - np.arange(1, sequence_length + 1) * (np.sum(random_sequence) / sequence_length)
        return np.max(np.abs(cumulative_sum_random))

    @staticmethod
    def adaptive_statistical_test(sequence: str, significance_level=0.01, num_simulations=1000):
        """
        Perform the Adaptive Statistical Test on a binary sequence and calculate the p-value.
        
        Parameters:
            sequence (str): A binary sequence (0s and 1s).
            significance_level (float): The significance level for the test (default 0.01).
            num_simulations (int): Number of random sequences to generate for p-value calculation.
            
        Returns:
            tuple: (p_value, bool) where bool indicates if the sequence is random.
        """
        # Clean the sequence to remove spaces or any non-binary characters
        sequence = ''.join([bit for bit in sequence if bit in {'0', '1'}])
        n = len(sequence)
        
        if n == 0:
            return -1, False
        
        # Convert the sequence to an array of integers (0s and 1s)
        data = np.array([int(bit) for bit in sequence])
        
        # Count the number of 0s and 1s
        num_ones = np.sum(data)
        
        # Calculate the observed mean and variance
        p_hat = num_ones / n
        
        # Calculate the cumulative sum of deviations from the expected mean
        cumulative_sum = np.cumsum(data) - np.arange(1, n + 1) * p_hat
        max_deviation = np.max(np.abs(cumulative_sum))
        
        # Generate random sequences for p-value calculation in parallel
        random_deviations = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(AdaptiveStatisticalTest.generate_random_deviation, n) for _ in range(num_simulations)]
            for future in as_completed(futures):
                random_deviations.append(future.result())

        # Calculate p-value
        p_value = np.sum(np.array(random_deviations) >= max_deviation) / num_simulations
        
        # Ensure p_value is accurate up to 16 digits
        p_value = round(p_value, 16)

        # Return p_value and the test result based on significance level
        return (p_value, p_value >= significance_level)
