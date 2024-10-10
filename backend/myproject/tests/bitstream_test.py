import numpy as np
from scipy.stats import chi2

class BitstreamTest:
    @staticmethod
    def BitstreamTest(data, verbose=False):
        # Clean the input string: keep only '0' and '1'
        clean_data = ''.join(filter(lambda x: x in '01', data))
        
        if len(clean_data) == 0:
            return -1, False  # Return a default value if no valid binary data

        # Convert the cleaned string of binary data to a list of integers (0s and 1s)
        data_array = np.array([int(bit) for bit in clean_data], dtype=int)  # Convert to integer array
        
        # Check if all elements are either 0 or 1
        if np.any((data_array < 0) | (data_array > 1)):
            raise ValueError("Data should contain only binary values (0 or 1).")
        
        n = len(data_array)
        bitstream = np.packbits(data_array)  # Pack the bits into bytes
        expected = n / 256  # Expect uniform distribution over 256 possible byte values
        counts = np.bincount(bitstream, minlength=256)  # Count occurrences of each byte value
        chi_square = np.sum((counts - expected) ** 2 / expected)  # Chi-square statistic
        p_value = 1 - chi2.cdf(chi_square, 255)  # Degrees of freedom = 256 - 1
        
        if verbose:
            print(f"Bitstream Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
