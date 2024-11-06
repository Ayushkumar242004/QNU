from math import sqrt
from scipy.stats import norm
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class AutocorrelationTest:

    @staticmethod
    def _calculate_autocovariance(data: np.ndarray, lag: int, mean: float):
        """
        Helper function to calculate the autocovariance for a specific lag.
        
        Parameters:
            data (np.ndarray): The binary data as a NumPy array.
            lag (int): The lag to calculate the autocovariance for.
            mean (float): The mean of the data.

        Returns:
            float: The autocovariance for the specified lag.
        """
        # Calculate the autocovariance
        autocovariance = np.mean((data[:-lag] - mean) * (data[lag:] - mean))
        return autocovariance

    @staticmethod
    def autocorrelation_test(binary_data: str, max_lag: int = 20, verbose=False):
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
            return -1, False
        
        # Convert binary string to array of integers
        data = np.array([int(bit) for bit in binary_data])
        
        # Calculate the mean of the sequence
        mean = np.mean(data)

        # Calculate the variance of the sequence
        variance = np.var(data)

        # Calculate the autocorrelations in parallel
        autocorrelations = []

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(AutocorrelationTest._calculate_autocovariance, data, lag, mean): lag for lag in range(1, max_lag + 1)}
            for future in as_completed(futures):
                lag = futures[future]
                autocovariance = future.result()
                autocorrelations.append(autocovariance / variance)  # Normalize by variance
        
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