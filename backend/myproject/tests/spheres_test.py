import numpy as np  # Import numpy for numerical operations
from scipy.stats import norm  # Import norm for the normal distribution

class Spheres3DTest:
    @staticmethod
    def Spheres3DTest(data, verbose=False):
        if len(data) < 3:  # Ensure there are enough data points for at least one 3D point
            return -1, False  # Return (-1, False) for insufficient data
        
        try:
            # Ensure data consists of floats or integers
            data = [float(bit) for bit in data]
        except ValueError:
            return -1, False  # Return (-1, False) if conversion fails
        
        n = len(data) // 3  # Split data into 3D coordinates
        points = [(data[3*i], data[3*i+1], data[3*i+2]) for i in range(n)]
        
        # Count how many points lie inside the unit sphere (radius <= 1)
        inside_sphere = np.sum([1 for point in points if np.linalg.norm(point) <= 1])
        
        # Expected number of points inside the unit sphere
        expected = n * (4 / 3) * np.pi * (1**3)  # Volume of the unit sphere
        
        # Variance based on the test literature
        variance = n * ((4 / 3) * np.pi) * (1 - (4 / 3) * np.pi)
        
        # Z-statistic and p-value calculation
        z_statistic = (inside_sphere - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        
        if verbose:
            print(f"3D Spheres Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
