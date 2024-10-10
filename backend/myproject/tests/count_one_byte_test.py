class CountThe1sByteTest:
    @staticmethod
    def CountThe1sByteTest(data, verbose=False):
        n = len(data) // 8
        ones_counts = [np.sum(data[i*8:(i+1)*8]) for i in range(n)]
        expected = 4
        variance = 2
        chi_square = np.sum([(count - expected) ** 2 / variance for count in ones_counts])
        p_value = 1 - chi2.cdf(chi_square, n - 1)
        
        if verbose:
            print(f"Count-the-1s (Byte) Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
