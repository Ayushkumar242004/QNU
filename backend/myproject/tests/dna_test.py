from scipy.stats import chi2  # Import chi2 for the chi-square test

class DNATest:
    @staticmethod
    def DNATest(data, verbose=False):
        # Check for empty input data
        if data is None or len(data) == 0:
            return -1, False
        
        if not isinstance(data, (list, str)) or len(data) < 10:
            return -1, False
        
        n = len(data)
        subsequences = set()
        
        # Extract subsequences of length 10
        for i in range(n - 9):
            subseq = tuple(data[i:i + 10])
            subsequences.add(subseq)
        
        observed = len(subsequences)
        expected = 1024  # 2^10 = 1024 possible binary subsequences
        chi_square = ((observed - expected) ** 2) / expected
        
        # Calculate the p-value
        p_value = 1 - chi2.cdf(chi_square, 1023)  # 1024-1 = 1023 degrees of freedom
        
        if verbose:
            print(f"DNA Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)  # Return p-value and pass/fail result
