import numpy as np
from scipy.stats import chi2

class BirthdaySpacingsTest:
    @staticmethod
    def BirthdaySpacingsTest(data, t=512, verbose=False):
        if len(data) < 2:
            raise ValueError("Insufficient data. At least two data points are required.")
        
        # Apply modulus operation to each element in the data array
        mod_data = np.array(data) % t  # Convert to numpy array and apply modulus
        
        spacings = np.diff(np.sort(mod_data))  # Now this will work correctly
        k = len(spacings)
        
        if np.mean(spacings) == 0:
            raise ValueError("Mean of spacings is zero, cannot perform test.")
        
        chi_square = (np.var(spacings) / np.mean(spacings)) * (k - 1)
        p_value = 1 - chi2.cdf(chi_square, k - 1)
        
        if verbose:
            print(f"Birthday Spacings Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
