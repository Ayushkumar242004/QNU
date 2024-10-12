import numpy as np
from scipy.stats import chi2

class BirthdaySpacingsTest:
    @staticmethod
    def BirthdaySpacingsTest(data, t=512, verbose=False):

        if not data:
            return -1, False
        # Return -1, False if no data or insufficient data
        if len(data) < 2:
            return -1, False
        
        try:
            # Apply modulus operation to each element in the data array
            mod_data = np.array(data) % t  # Convert to numpy array and apply modulus
            
            spacings = np.diff(np.sort(mod_data))  # Calculate spacings
            k = len(spacings)

            if k == 0 or np.mean(spacings) == 0:
                return -1, False  # Handle cases where spacings are empty or mean is zero
            
            chi_square = (np.var(spacings) / np.mean(spacings)) * (k - 1)
            p_value = 1 - chi2.cdf(chi_square, k - 1)
            
            if verbose:
                print(f"Birthday Spacings Test - Chi-square: {chi_square}, p-value: {p_value}")
            
            return p_value, (p_value >= 0.01)  # Return p-value and pass/fail result

        except Exception as e:
            # Catch any other exceptions and return -1, False
            print(f"Error: {e}")
            return -1, False
