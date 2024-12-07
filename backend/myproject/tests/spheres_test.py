import numpy as np
from scipy.stats import norm
from concurrent.futures import ThreadPoolExecutor

class Spheres3DTest:
    @staticmethod
    def Spheres3DTest(data, verbose=False):
        # Step 1: Sanitize input by removing commas and whitespace
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Step 2: Ensure we have at least one full 3D point (3 coordinates)
        if len(data) < 3:
            return -2, False  # Insufficient data, return failure result
        
        # Step 3: Convert binary string to numeric (float) data using NumPy for efficient processing
        try:
            data = np.array(list(map(float, data)), dtype=np.float64)
        except ValueError:
            return -7, False  # Invalid data format, return failure

        # Step 4: Split data into 3D points (x, y, z coordinates)
        n = len(data) // 3  # Calculate the number of 3D points
        if n == 0:
            return -2, False  # No valid 3D points

        # Reshape the data into an array of shape (n, 3), where each row is a 3D point
        points = data[:n * 3].reshape(n, 3)

        # Step 5: Use ThreadPoolExecutor for parallel computation of Euclidean norms (distances from the origin)
        with ThreadPoolExecutor() as executor:
            distances = list(executor.map(np.linalg.norm, points))

        distances = np.array(distances)  # Convert to numpy array for further calculations

        # Step 6: Count points that are inside the unit sphere (distance <= 1) in parallel
        with ThreadPoolExecutor() as executor:
            inside_sphere_counts = list(executor.map(lambda d: d <= 1, distances))

        inside_sphere = np.sum(inside_sphere_counts)  # Sum up the True counts

        # Step 7: Compute the expected number of points inside the sphere using volume of unit sphere
        expected = n * (4 / 3) * np.pi  # Volume of unit sphere (radius = 1)

        # Step 8: Compute the variance (as per literature) and handle edge cases
        variance = n * ((4 / 3) * np.pi) * (1 - (4 / 3) * np.pi)
        if variance <= 0:
            return -1, False  # Invalid variance, return failure

        # Step 9: Calculate Z-statistic and p-value
        z_statistic = (inside_sphere - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        # Step 10: Optional verbose output for debugging
        if verbose:
            print(f"3D Spheres Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        # Return the p-value and whether it passes the significance threshold (0.01)
        return p_value, (p_value >= 0.01)