import numpy as np
from scipy.stats import chi2  # Import chi2 for Chi-square distribution

class OPSOTest:
    @staticmethod
    def OPSOTest(data, verbose=False):

        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 2:
            return -1, False  # Return (-1, False) if insufficient data
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)  # Convert to integer array
        
        # Generate pairs and count unique pairs
        pairs = set()
        for i in range(n - 1):
            pair = (data_array[i], data_array[i + 1])
            pairs.add(pair)
        
        observed = len(pairs)  # Number of unique pairs
        expected = 4  # 2^2 = 4 possible binary pairs
        chi_square = ((observed - expected) ** 2) / expected
        
        # Chi-square test
        p_value = 1 - chi2.cdf(chi_square, 3)  # 4-1 = 3 degrees of freedom
        
        if verbose:
            print(f"OPSO Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)


