import numpy as np
from scipy.stats import chi2  # Import chi2 for Chi-square distribution

class OQSOTest:
    @staticmethod
    def OQSOTest(data, verbose=False):
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        # Check if we have enough data
        n = len(clean_data)
        if n < 4:
            return -1, False  # Return (-1, False) if insufficient data
        
        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)  # Convert to integer array
        
        # Generate quadruples and count unique quadruples
        quads = set()
        for i in range(n - 3):
            quad = (data_array[i], data_array[i + 1], data_array[i + 2], data_array[i + 3])
            quads.add(quad)
        
        observed = len(quads)  # Number of unique quadruples
        expected = 16  # 2^4 = 16 possible binary quadruples
        chi_square = ((observed - expected) ** 2) / expected
        
        # Chi-square test
        p_value = 1 - chi2.cdf(chi_square, 15)  # 16-1 = 15 degrees of freedom
        
        if verbose:
            print(f"OQSO Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)


