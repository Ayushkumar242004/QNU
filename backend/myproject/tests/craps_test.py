import numpy as np
from scipy.stats import norm

class CrapsTest:
    @staticmethod
    def CrapsTest(data, verbose=False):
        wins = 0
        losses = 0
        i = 0
        
        try:
            # Ensure data is numeric (convert bits to integers)
            data = [int(bit) for bit in data]
        except ValueError:
            return -1, False  # Return (-1, False) if data contains invalid characters
        
        while i < len(data):
            roll = data[i:i + 2]  # Take pairs of bits as dice rolls
            if len(roll) < 2:
                break  # Ignore incomplete pairs
            
            # Sum the roll after ensuring both elements are integers
            outcome = sum(roll)
            
            if outcome in [2, 3, 12]:  # Loss on first roll
                losses += 1
            elif outcome in [7, 11]:  # Win on first roll
                wins += 1
            else:
                point = outcome
                # Keep rolling until 7 or point is matched
                while True:
                    i += 2
                    if i >= len(data):
                        break
                    next_roll = sum(data[i:i + 2])
                    if next_roll == point:
                        wins += 1
                        break
                    elif next_roll == 7:
                        losses += 1
                        break
            i += 2
        
        total_games = wins + losses
        if total_games == 0:
            return -1, False  # Handle case when no games were played
        
        # Expected wins based on craps probabilities
        expected_wins = total_games * (244 / 495)  # Approximate win probability in craps
        variance = total_games * (244 / 495) * (1 - (244 / 495))
        z_statistic = (wins - expected_wins) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        
        if verbose:
            print(f"Craps Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
