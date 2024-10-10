from math import sqrt
from scipy.stats import norm
import numpy as np

class GeneralizedMinimumDistanceTest:
    @staticmethod
    def GeneralizedMinimumDistanceTest(data, d=2, verbose=False):
        n = len(data)
        coords = np.array([data[i:i + d] for i in range(n - d + 1)])
        distances = np.array([np.linalg.norm(coords[i] - coords[i + 1]) for i in range(len(coords) - 1)])
        mean_distance = np.mean(distances)
        expected = sqrt(d) / 2
        variance = np.var(distances)
        z_statistic = (mean_distance - expected) / sqrt(variance / len(distances))
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Generalized Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
