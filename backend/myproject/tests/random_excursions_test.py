from concurrent.futures import ThreadPoolExecutor, as_completed
from scipy.special import gammaincc, erfc
from numpy import array, where, transpose, clip, sum, sqrt

class RandomExcursions:
    @staticmethod
    def get_frequency(data, value):
        """Counts the occurrences of 'value' in 'data'."""
        return data.count(value)

    @staticmethod
    def get_pi_value(uu, target_state):
        """Calculates the pi value based on uu and target_state."""
        pi_values = {
            -4: 0.000671,
            -3: 0.008911,
            -2: 0.037507,
            -1: 0.124931,
             0: 0.242731,
             1: 0.124931,
             2: 0.037507,
             3: 0.008911,
             4: 0.000671
        }
        return pi_values.get(uu, 0)

    @staticmethod
    def random_excursions_test(binary_data: str, target_state=-1):
        try:
            # Convert binary string to +1 and -1 steps
            li_data = [1 if bit == '1' else -1 for bit in binary_data]
            cumulative_sum = [0] + [sum(li_data[:i+1]) for i in range(len(li_data))]

            cycles = []
            start_idx = 0
            # Create cycles between zero-crossings
            for i in range(1, len(cumulative_sum)):
                if cumulative_sum[i] == 0:
                    cycles.append(array(cumulative_sum[start_idx:i+1]))
                    start_idx = i

            # Parallelize state count calculations for cycles
            def calculate_state_counts(cycles_batch):
                return [len(where(cycle == target_state)[0]) for cycle in cycles_batch]

            # Split cycles for parallel processing
            batch_size = max(1, len(cycles) // 8)
            cycles_batches = [cycles[i:i + batch_size] for i in range(0, len(cycles), batch_size)]
            
            state_count = []
            with ThreadPoolExecutor() as executor:
                futures = {executor.submit(calculate_state_counts, batch): batch for batch in cycles_batches}
                for future in as_completed(futures):
                    state_count.extend(future.result())
            
            state_count = clip(array(state_count), 0, 5)

            # Calculate observed values and expected values
            su = [(state_count == cycle).sum() for cycle in range(6)]
            
            num_cycles = len(cycles)
            pi = array([RandomExcursions.get_pi_value(uu, target_state) for uu in range(6)])
            inner_term = num_cycles * pi

            # Add epsilon to avoid divide-by-zero errors
            epsilon = 1e-10
            xObs = sum((array(su) - inner_term) ** 2 / (inner_term + epsilon))
            chi_sq = xObs
            p_value = gammaincc(2.5, xObs / 2.0)
            
            result = p_value >= 0.01
            return chi_sq, p_value, result

        except Exception as e:
            # Log the exception if necessary
            print(f"Error in random_excursions_test: {e}")
            return -4, False

    @staticmethod
    def variant_test(binary_data: str, target_state=1, verbose=False):
        # Convert binary string to +1 and -1 steps
        li_data = [1 if bit == '1' else -1 for bit in binary_data]
        cumulative_sum = [0] + [sum(li_data[:i+1]) for i in range(len(li_data))]

        index = list(set(cumulative_sum))

        # Parallelize p-value calculation
        def calculate_p_values(counts_batch):
            j = RandomExcursions.get_frequency(li_data, 0) + 1
            p_values_batch = []
            for count in counts_batch:
                if count != 0:
                    den = sqrt(2 * j * (4 * abs(count) - 2))
                    p_values_batch.append(erfc(abs(RandomExcursions.get_frequency(li_data, count) - j) / den))
            return p_values_batch

        # Split index for parallel processing
        batch_size = max(1, len(index) // 8)
        index_batches = [index[i:i + batch_size] for i in range(0, len(index), batch_size)]

        p_values = []
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(calculate_p_values, batch): batch for batch in index_batches}
            for future in as_completed(futures):
                p_values.extend(future.result())

        # Remaining calculations for chi-square and p-value
        state_count = [li_data.count(cycle) for cycle in range(6)]
        num_cycles = len(li_data)
        pi = array([RandomExcursions.get_pi_value(uu, target_state) for uu in range(6)])
        inner_term = num_cycles * pi
        
        # Add epsilon to avoid divide-by-zero errors
        epsilon = 1e-10
        xObs = sum((array(state_count) - inner_term) ** 2 / (inner_term + epsilon))
        chi_sq = xObs
        p_value = gammaincc(2.5, xObs / 2.0)

        result = p_value >= 0.01
        return chi_sq, p_value, result
