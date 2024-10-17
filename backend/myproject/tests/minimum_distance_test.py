import numpy as np
from scipy.stats import norm
from sklearn.neighbors import KDTree  # Use KDTree for nearest neighbor search

class MinimumDistanceTest:
    @staticmethod
    def MinimumDistanceTest(data, verbose=False):
        # Sanitize input by removing non-binary characters (e.g., commas, spaces)
        data = data.replace(',', '').replace(' ', '').strip()

        if not data:
            return None 
        
        # Ensure that data length is even (to split into 2D coordinates)
        if len(data) < 4 or len(data) % 2 != 0:
            return -1, False  # Not enough data to form at least 2 points

        try:
            # No need to convert to integers, operate directly with binary string
            n = len(data) // 2  # Number of 2D points

            # Create 2D points directly as numpy array (for efficient storage)
            points = np.array([[int(data[2 * i]), int(data[2 * i + 1])] for i in range(n)])
        except ValueError:
            return -1, False  # Return failure if data contains invalid characters

        try:
            # Use KDTree for efficient nearest neighbor search
            tree = KDTree(points)

            # Query each point for its nearest neighbor
            distances, _ = tree.query(points, k=2)  # k=2 to exclude the point itself

            # The second column of distances gives the nearest neighbor (excluding the point itself)
            min_distances = distances[:, 1]  # Take the nearest neighbor distance for each point

            # Expected distance and variance from test literature
            expected = np.sqrt(2 / (np.pi * n))
            variance = 0.07  # Approximation from literature

            # Calculate Z-statistic and p-value
            z_statistic = (np.mean(min_distances) - expected) / np.sqrt(variance)
            p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

            if verbose:
                print(f"Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")

            return p_value, (p_value >= 0.01)

        except Exception as e:
            return -1, False  # Catch-all for any unexpected issues
