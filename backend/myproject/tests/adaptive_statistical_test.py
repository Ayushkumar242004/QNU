import numpy as np

class AdaptiveStatisticalTest:

    @staticmethod
    def adaptive_statistical_test(sequence: str, significance_level=0.01, num_simulations=1000):
        """
        Perform the Adaptive Statistical Test on a binary sequence and calculate the p-value.
        
        Parameters:
            sequence (str): A binary sequence (0s and 1s).
            significance_level (float): The significance level for the test (default 0.05).
            num_simulations (int): Number of random sequences to generate for p-value calculation.
            
        Returns:
            tuple: (p_value, bool) where bool indicates if the sequence is random.
        """
        # Clean the sequence to remove spaces or any non-binary characters
        sequence = ''.join([bit for bit in sequence if bit in {'0', '1'}])
        n = len(sequence)
        
        if n == 0:
            raise ValueError("The sequence must not be empty or contain only non-binary characters.")
        
        # Convert the sequence to an array of integers (0s and 1s)
        data = np.array([int(bit) for bit in sequence])
        
        # Count the number of 0s and 1s
        num_ones = np.sum(data)
        
        # Calculate the observed mean and variance
        p_hat = num_ones / n
        
        # Calculate the cumulative sum of deviations from the expected mean
        cumulative_sum = np.cumsum(data) - np.arange(1, n + 1) * p_hat
        max_deviation = np.max(np.abs(cumulative_sum))
        
        # Generate random sequences for p-value calculation
        random_deviations = []
        for _ in range(num_simulations):
            random_sequence = np.random.choice([0, 1], size=n)
            cumulative_sum_random = np.cumsum(random_sequence) - np.arange(1, n + 1) * (np.sum(random_sequence) / n)
            random_max_deviation = np.max(np.abs(cumulative_sum_random))
            random_deviations.append(random_max_deviation)

        # Calculate p-value
        p_value = np.sum(np.array(random_deviations) >= max_deviation) / num_simulations

        # Ensure p_value is accurate up to 16 digits
        p_value = round(p_value, 16)

        # Return p_value and the test result based on significance level
        return (p_value, p_value >= significance_level)
