class CountThe1sStreamTest:
    @staticmethod
    def CountThe1sStreamTest(data, verbose=False):
        n = len(data)
        ones_count = np.sum(data)
        expected = n / 2
        variance = n / 4
        z_statistic = (ones_count - expected) / sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        
        if verbose:
            print(f"Count-the-1s (Stream) Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
