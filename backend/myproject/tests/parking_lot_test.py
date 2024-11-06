import numpy as np
from scipy.stats import norm
from concurrent.futures import ThreadPoolExecutor, as_completed

class ParkingLotTest:
    @staticmethod
    def _compute_distances(coordinates_chunk):
        """Helper function to compute distances for a chunk of coordinates."""
        return np.linalg.norm(coordinates_chunk, axis=1)

    @staticmethod
    def ParkingLotTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Step 1: Sanitize and validate input
        if not data or len(data.strip()) % 2 != 0:
            return -1, False

        # Remove commas or spaces, then convert to numpy array of integers (0 or 1)
        data = np.fromiter(map(int, data.replace(',', '').strip()), dtype=np.int8)

        n = len(data) // 2  # Each pair represents coordinates
        if n == 0:
            return -1, False  # Not enough data to form even a single point

        # Step 2: Reshape the data into coordinates (2D array with two columns)
        coordinates = data.reshape(n, 2)
        
        # Step 3: Parallel distance calculation
        num_chunks = min(4, n)  # Set number of chunks based on data length or desired parallelism
        chunk_size = n // num_chunks

        distances = []
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in range(num_chunks):
                start = i * chunk_size
                end = (i + 1) * chunk_size if i < num_chunks - 1 else n
                futures.append(executor.submit(ParkingLotTest._compute_distances, coordinates[start:end]))

            for future in as_completed(futures):
                distances.extend(future.result())

        distances = np.array(distances)

        # Count points inside the unit circle (radius <= 1)
        parked = np.sum(distances < 1)

        # Step 4: Statistical analysis
        expected = n * np.pi / 4
        variance = n * (np.pi / 4) * (1 - (np.pi / 4))
        
        if variance == 0:
            return -1, False  # Avoid division by zero if variance is zero
        
        z_statistic = (parked - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        # Step 5: Verbose output (optional)
        if verbose:
            print(f"Parking Lot Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)
