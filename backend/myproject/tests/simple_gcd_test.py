import numpy as np
import math
from scipy.stats import chi2
from concurrent.futures import ThreadPoolExecutor

class MarsagliaTsangSimpleGCDTest:
    @staticmethod
    def MarsagliaTsangSimpleGCDTest(data, verbose=False):

        # Clean and validate the input data
        data = data.replace(',', '').strip()
        if not data:
            return None
        if data is None or len(data) == 0:
            return -2, False

        try:
            # Preprocess the input data to remove invalid characters
            cleaned_data = []
            for item in data:
                cleaned_items = ''.join(filter(str.isdigit, item)).split()
                for cleaned_item in cleaned_items:
                    cleaned_data.append(int(cleaned_item))

            # Convert to numpy array of integers
            data = np.array(cleaned_data, dtype=int)

            # Ensure the input data length is even for pairing
            if len(data) % 2 != 0:
                raise ValueError("Input data length must be even.")

            # Function to compute GCD for a given pair index
            def compute_gcd_for_pair(i):
                gcd_val = math.gcd(data[i], data[i + 1])
                return 1 if gcd_val == 1 else 0

            # Use ThreadPoolExecutor to parallelize GCD computation
            with ThreadPoolExecutor() as executor:
                gcd_counts = list(executor.map(compute_gcd_for_pair, range(0, len(data), 2)))

            # Expected probability that GCD of two random integers is 1
            expected_prob = 6 / (np.pi ** 2)

            # Calculate observed and expected counts of GCD=1
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

            # Return p-value and pass/fail based on the p-value threshold
            return p_value, (p_value >= 0.01)

        except ValueError as e:
            print(f"ValueError: {e}")
            return -7, False  # Return -1 if there's a ValueError
        except Exception as e:
            print(f"Error: {e}")
            return -4, False  # Return -1 for any other error