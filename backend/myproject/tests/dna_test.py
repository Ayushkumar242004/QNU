from scipy.stats import chi2  # Import chi2 for the chi-square test

class DNATest:
    @staticmethod
    def DNATest(data, verbose=False):
        n = len(data)
        subsequences = set()
        for i in range(n - 9):
            subseq = tuple(data[i:i + 10])
            subsequences.add(subseq)
        
        observed = len(subsequences)
        expected = 1024  # 2^10 = 1024 possible binary subsequences
        chi_square = ((observed - expected) ** 2) / expected
        p_value = 1 - chi2.cdf(chi_square, 1023)  # 1024-1 = 1023 degrees of freedom
        
        if verbose:
            print(f"DNA Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
