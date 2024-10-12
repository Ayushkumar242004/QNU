import numpy as np
from scipy.stats import norm

class ParkingLotTest:
    @staticmethod
    def ParkingLotTest(data, verbose=False):
        if not data:
            return -1, False
        # Sanitize the input to remove any non-binary characters like ',' or spaces
        data = data.replace(',', '').strip()
        
        
        
        if len(data) % 2 != 0:
            return -1, False
        
        n = len(data) // 2  # Assume each pair represents coordinates
        
        # Convert binary data pairs into numeric coordinates (0 or 1)
        coordinates = [(int(data[2 * i]), int(data[2 * i + 1])) for i in range(n)]
        
        parked = 0
        for coord in coordinates:
            if np.linalg.norm(coord) < 1:  # Check if inside a unit circle
                parked += 1
        
        expected = n * np.pi / 4
        variance = n * (np.pi / 4) * (1 - (np.pi / 4))
        z_statistic = (parked - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        
        if verbose:
            print(f"Parking Lot Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
