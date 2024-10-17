import numpy as np
from scipy.stats import norm

class CrapsTest:
    @staticmethod
    def CrapsTest(data, verbose=False):
        # Step 1: Sanitize input by removing commas and spaces
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Step 2: Convert data into a NumPy array of integers (0 or 1)
        try:
            data = np.array(list(map(int, data)), dtype=np.int8)
        except ValueError:
            return -1, False  # Invalid data, return failure
        
        # Step 3: Ensure there are enough bits to form rolls
        if len(data) < 2:
            return -1, False  # Insufficient data, return failure
        
        wins = 0
        losses = 0
        i = 0

        # Step 4: Process dice rolls in pairs (representing 2-bit chunks as dice outcomes)
        while i + 1 < len(data):
            roll = data[i:i + 2]  # Take 2-bit pairs to simulate dice rolls
            outcome = np.sum(roll)  # Sum the two bits to get the outcome
            
            if outcome in [2, 3, 12]:  # Loss on first roll
                losses += 1
            elif outcome in [7, 11]:  # Win on first roll
                wins += 1
            else:
                point = outcome
                # Step 5: Continue rolling until a 7 or the point is matched
                while True:
                    i += 2
                    if i + 1 >= len(data):
                        break
                    next_roll = np.sum(data[i:i + 2])
                    if next_roll == point:
                        wins += 1
                        break
                    elif next_roll == 7:
                        losses += 1
                        break
            i += 2

        total_games = wins + losses
        if total_games == 0:
            return -1, False  # No games played, return failure

        # Step 6: Calculate expected wins and variance based on craps probabilities
        expected_wins = total_games * (244 / 495)  # Approximate win probability in craps
        variance = total_games * (244 / 495) * (1 - (244 / 495))

        # Step 7: Calculate Z-statistic and p-value for hypothesis testing
        z_statistic = (wins - expected_wins) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        # Step 8: Optional verbose output for debugging
        if verbose:
            print(f"Craps Test - Z-statistic: {z_statistic}, p-value: {p_value}")

        # Step 9: Return the p-value and result based on a significance level of 0.01
        return p_value, (p_value >= 0.01)
