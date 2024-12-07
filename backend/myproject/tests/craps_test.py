import numpy as np
from scipy.stats import norm
from concurrent.futures import ThreadPoolExecutor, as_completed

class CrapsTest:
    @staticmethod
    def process_chunk(chunk_data, previous_leftover=None):
        """Process a chunk of data for CrapsTest and return wins, losses, and leftover roll."""
        wins, losses = 0, 0
        leftover_roll = previous_leftover

        # If there was a leftover roll from the previous chunk, prepend it
        if leftover_roll is not None:
            chunk_data = np.concatenate(([leftover_roll], chunk_data))

        i = 0
        while i + 1 < len(chunk_data):
            roll = chunk_data[i:i + 2]
            if len(roll) < 2:
                leftover_roll = roll[0]
                break

            outcome = np.sum(roll)
            if outcome in [2, 3, 12]:
                losses += 1
            elif outcome in [7, 11]:
                wins += 1
            else:
                point = outcome
                while True:
                    i += 2
                    if i + 1 >= len(chunk_data):
                        leftover_roll = chunk_data[i] if i < len(chunk_data) else None
                        break
                    next_roll = np.sum(chunk_data[i:i + 2])
                    if next_roll == point:
                        wins += 1
                        break
                    elif next_roll == 7:
                        losses += 1
                        break
            i += 2

        return wins, losses, leftover_roll

    @staticmethod
    def CrapsTest(data, chunk_size=10**6, verbose=False):
        data = data.replace(',', '').strip()
        try:
            data = np.array(list(map(int, data)), dtype=np.int8)
        except ValueError:
            return -2, False  # Invalid data

        # Divide data into chunks for threading
        total_chunks = (len(data) + chunk_size - 1) // chunk_size  # Ceiling division
        chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(total_chunks)]

        # Track results from each thread
        total_wins, total_losses = 0, 0
        leftover_roll = None

        # Using ThreadPoolExecutor to process each chunk in parallel
        with ThreadPoolExecutor() as executor:
            futures = []
            for i, chunk in enumerate(chunks):
                futures.append(executor.submit(CrapsTest.process_chunk, chunk, leftover_roll))
                leftover_roll = None  # Only pass leftover for the first chunk

            for future in as_completed(futures):
                wins, losses, leftover = future.result()
                total_wins += wins
                total_losses += losses
                leftover_roll = leftover

        total_games = total_wins + total_losses
        if total_games == 0:
            return -2, False  # No games played

        expected_wins = total_games * (244 / 495)  # Approximate win probability in craps
        variance = total_games * (244 / 495) * (1 - (244 / 495))

        z_statistic = (total_wins - expected_wins) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Craps Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        return p_value, (p_value >= 0.01)