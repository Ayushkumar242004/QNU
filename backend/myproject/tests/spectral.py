from math import fabs, floor, log, sqrt
from concurrent.futures import ThreadPoolExecutor
from numpy import where, array, abs
from scipy import fftpack as sff
from scipy.special import erfc

class SpectralTest:
    @staticmethod
    def spectral_test(binary_data: str, verbose=False):
        # Clean binary_data to ensure it only contains '0's and '1's
        binary_data = ''.join(filter(lambda x: x in {'0', '1'}, binary_data))
        length_of_binary_data = len(binary_data)

        # Check if binary_data is empty after filtering
        if length_of_binary_data == 0:
            return -2, False  # Return (-2, False) if no valid input

        # Convert '0's and '1's to -1 and +1 using numpy array for parallel operation
        plus_one_minus_one = array([1 if char == '1' else -1 for char in binary_data])

        # Step 2 - Apply a Discrete Fourier Transform (DFT) on X
        spectral = sff.fft(plus_one_minus_one)

        # Step 3 - Calculate modulus
        slice_index = floor(length_of_binary_data / 2)
        modulus_values = spectral[0:slice_index]

        # Use ThreadPoolExecutor to compute modulus in parallel and convert to numpy array
        with ThreadPoolExecutor() as executor:
            modulus = array(list(executor.map(abs, modulus_values)))

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