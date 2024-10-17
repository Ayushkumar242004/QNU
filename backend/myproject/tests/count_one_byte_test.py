import numpy as np
from scipy.stats import chi2

class CountThe1sByteTest:
    @staticmethod
    def CountThe1sByteTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        if data is None or len(data) == 0:
            return -1, False
        
        # Clean and convert input data to integers
        try:
            # Validate and filter binary input data
            cleaned_data = []

            # Iterate through each item in the input data
            for item in data:
                # Remove whitespace and ignore invalid characters
                for char in item.strip():
                    if char in ['0', '1']:
                        cleaned_data.append(int(char))

            # Ensure the input data is a numpy array of integers (0s and 1s)
            data = np.array(cleaned_data, dtype=int)

            # Check if the length of data is a multiple of 8
            if len(data) % 8 != 0:
                raise ValueError("Input data length must be a multiple of 8.")

            n = len(data) // 8
            ones_counts = [np.sum(data[i*8:(i+1)*8]) for i in range(n)]
            expected = 4
            variance = 2
            chi_square = np.sum([(count - expected) ** 2 / variance for count in ones_counts])
            p_value = 1 - chi2.cdf(chi_square, n - 1)

            if verbose:
                print(f"Count-the-1s (Byte) Test - Chi-square: {chi_square}, p-value: {p_value}")

            return p_value, (p_value >= 0.01)  # Return p-value and boolean for pass/fail

        except ValueError as e:
            print(f"ValueError: {e}")
            return -1, False  # Return -1 if there's a ValueError
        except Exception as e:
            print(f"Error: {e}")
            return -1, False  # Return -1 for any other error
