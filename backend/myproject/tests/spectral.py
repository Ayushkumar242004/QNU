from math import fabs
from math import floor
from math import log
from math import sqrt
from numpy import where
from scipy import fftpack as sff
from scipy.special import erfc

class SpectralTest:

    @staticmethod
    def spectral_test(binary_data: str, verbose=False):
        """
        Perform the Spectral Test on the binary sequence.

        :param binary_data: The sequence of bits being tested.
        :param verbose: True to display the debug message, False to turn off debug message.
        :return: (p_value, bool) A tuple containing the p_value and result of the frequency test (True or False).
        """
        # Clean the binary_data to ensure it only contains '0's and '1's
        binary_data = ''.join(filter(lambda x: x in {'0', '1'}, binary_data))
        length_of_binary_data = len(binary_data)

        # Check if binary_data is empty after filtering
        if length_of_binary_data == 0:
            return -1, False  # Return (-1, False) if no valid input

        plus_one_minus_one = []

        # Convert '0's and '1's to -1 and +1
        for char in binary_data:
            if char == '0':
                plus_one_minus_one.append(-1)
            elif char == '1':
                plus_one_minus_one.append(1)

        # Step 2 - Apply a Discrete Fourier Transform (DFT) on X
        spectral = sff.fft(plus_one_minus_one)

        # Step 3 - Calculate modulus
        slice_index = floor(length_of_binary_data / 2)
        modulus = abs(spectral[0:slice_index])

        # Step 4 - Compute the threshold value T
        tau = sqrt(log(1 / 0.05) * length_of_binary_data)

        # Step 5 - Compute N0 (expected number of peaks)
        n0 = 0.95 * (length_of_binary_data / 2)

        # Step 6 - Compute N1 (observed number of peaks)
        n1 = len(where(modulus < tau)[0])

        # Step 7 - Compute d
        d = (n1 - n0) / sqrt(length_of_binary_data * (0.95) * (0.05) / 4)

        # Step 8 - Compute p_value
        p_value = erfc(fabs(d) / sqrt(2))

        if verbose:
            print('Discrete Fourier Transform (Spectral) Test:')
            print('\tP-Value:\t\t\t\t', p_value)

        return p_value, (p_value >= 0.01)
