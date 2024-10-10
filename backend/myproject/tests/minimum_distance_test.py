import numpy as np
from scipy.stats import norm

class MinimumDistanceTest:
    @staticmethod
    def MinimumDistanceTest(data, verbose=False):
        # Sanitize input by removing non-binary characters (e.g., commas, spaces)
        data = data.replace(',', '').replace(' ', '').strip()

        # Ensure that data length is even (to split into 2D coordinates)
        if len(data) < 4 or len(data) % 2 != 0:
            return -1, False  # Not enough data to form at least 2 points

        try:
            # Convert the sanitized binary string to a list of integers
            data = [int(bit) for bit in data]
        except ValueError:
            return -1, False  # Return failure if data contains invalid characters

        n = len(data) // 2  # Split data into 2D coordinates
        points = [(data[2*i], data[2*i+1]) for i in range(n)]
        min_distances = []

        for i in range(n):
            # Calculate distances from point i to all other points
            dists = [np.linalg.norm(np.array(points[i]) - np.array(points[j])) for j in range(n) if i != j]
            
            if dists:  # Ensure dists is not empty
                min_distances.append(min(dists))
            else:
                return -1, False  # If no distances can be calculated, return failure

        # Expected distance and variance from test literature
        expected = np.sqrt(2 / (np.pi * n))
        variance = 0.07  # Approximation from literature
        z_statistic = (np.mean(min_distances) - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)
