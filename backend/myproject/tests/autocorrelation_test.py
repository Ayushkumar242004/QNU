from math import sqrt
from scipy.stats import norm
import numpy as np

class AutocorrelationTest:

    @staticmethod
    def autocorrelation_test(binary_data: str, max_lag: int, verbose=False):
        """
        Perform the Autocorrelation Test on a binary sequence to check for randomness.
        
        Parameters:
            binary_data (str): A binary sequence (0s and 1s).
            max_lag (int): The maximum lag to test the autocorrelation.
            verbose (bool): If True, prints detailed debug information.
        
        Returns:
            tuple: (p_value, bool) where bool indicates if the sequence is random.
        """
        # Clean the input by removing any spaces or invalid characters
        binary_data = ''.join([bit for bit in binary_data if bit in ['0', '1']])

        n = len(binary_data)
        
        if n <= max_lag:
            raise ValueError("The length of the binary sequence must be greater than the maximum lag.")
        
        # Convert binary string to array of integers
        data = np.array([int(bit) for bit in binary_data])
        
        # Calculate the mean of the sequence
        mean = np.mean(data)
        
        # Calculate the autocorrelations
        autocorrelations = []
        for lag in range(1, max_lag + 1):
            autocovariance = np.mean((data[:-lag] - mean) * (data[lag:] - mean))
            autocorrelations.append(autocovariance / np.var(data))
        
        # Calculate the test statistic
        z_statistic = np.sqrt(n) * np.sum(autocorrelations)
        
        # Calculate p-value
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))  # Two-tailed test

        if verbose:
            print('Autocorrelation Test:')
            print('\tZ-Statistic:\t\t', z_statistic)
            print('\tP-Value:\t\t', p_value)

        # Return p_value and result of the test
        return (p_value, (p_value >= 0.01))