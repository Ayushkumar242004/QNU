from math import sqrt
from scipy.stats import norm
import numpy as np

class GeneralizedMinimumDistanceTest:
    @staticmethod
    def GeneralizedMinimumDistanceTest(data, d=2, verbose=False):
        try:
            # Convert input data to numeric values (float) if they are in string format
            cleaned_data = []
            for x in data:
                try:
                    cleaned_data.append(float(x))  # Convert each element to float
                except ValueError:
                    # If conversion fails, ignore the invalid input
                    continue

            # Ensure the input is now cleaned and contains numeric values
            cleaned_data = np.array(cleaned_data, dtype=float)

            # Check if there are enough data points for the given dimension
            n = len(cleaned_data)
            if n < d + 1:
                return -1, False  # Not enough data points for the test

            # Reshape data into coordinates of dimension 'd'
            coords = np.array([cleaned_data[i:i + d] for i in range(n - d + 1)])

            # Compute distances between consecutive coordinate pairs
            distances = np.array([np.linalg.norm(coords[i] - coords[i + 1]) for i in range(len(coords) - 1)])

            # Calculate mean and expected distance
            mean_distance = np.mean(distances)
            expected = sqrt(d) / 2
            variance = np.var(distances)

            # Calculate Z-statistic
            z_statistic = (mean_distance - expected) / sqrt(variance / len(distances))
            p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

            if verbose:
                print(f"Generalized Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")
            
            # Return p-value and pass/fail result (p-value >= 0.01 passes the test)
            return p_value, (p_value >= 0.01)

        except Exception as e:
            print(f"Error: {e}")
            return -1, False  # Return -1 for any other error
