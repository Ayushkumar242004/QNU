import numpy as np
import math
from scipy.stats import chi2

class MarsagliaTsangSimpleGCDTest:
    @staticmethod
    def MarsagliaTsangSimpleGCDTest(data, verbose=False):

        data = data.replace(',', '').strip()

        if not data:
            return None 

        if data is None or len(data) == 0:
            return -1, False
        try:
            
            # Preprocess the input data to remove invalid characters (e.g., commas, spaces)
            cleaned_data = []
            for item in data:
                # Split the string by non-numeric characters and filter out empty strings
                cleaned_items = ''.join(filter(str.isdigit, item)).split()
                for cleaned_item in cleaned_items:
                    cleaned_data.append(int(cleaned_item))

            # Ensure the input data is a numpy array of integers
            data = np.array(cleaned_data, dtype=int)

            # The length of the dataset should be even since we take pairs
            if len(data) % 2 != 0:
                raise ValueError("Input data length must be even.")

            # Compute GCD of consecutive pairs
            gcd_counts = []
            for i in range(0, len(data), 2):
                gcd_val = math.gcd(data[i], data[i + 1])
                gcd_counts.append(1 if gcd_val == 1 else 0)

            # The expected probability that GCD of two random integers is 1
            expected_prob = 6 / (np.pi ** 2)

            # Calculate the observed and expected counts of GCD=1
            observed_gcd_1 = np.sum(gcd_counts)
            total_pairs = len(gcd_counts)
            expected_gcd_1 = expected_prob * total_pairs

            # Variance based on binomial distribution
            variance = total_pairs * expected_prob * (1 - expected_prob)

            # Calculate chi-square statistic
            chi_square = ((observed_gcd_1 - expected_gcd_1) ** 2) / variance
            p_value = 1 - chi2.cdf(chi_square, 1)

            if verbose:
                print(f"Marsaglia-Tsang Simple GCD Test - Chi-square: {chi_square}, p-value: {p_value}")
                # print(f"Observed GCD=1 Count: {observed_gcd_1}, Expected: {expected_gcd_1}")

            # Return p-value and whether the test passes (p-value >= 0.01 for randomness)
            return p_value, (p_value >= 0.01)

        except ValueError as e:
            print(f"ValueError: {e}")
            return -1, False  # Return -1 if there's a ValueError
        except Exception as e:
            print(f"Error: {e}")
            return -1, False  # Return -1 for any other error
