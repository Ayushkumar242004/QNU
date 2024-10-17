from scipy.stats import chi2  # Import chi2 for the chi-square test

class DNATest:
    @staticmethod
    def DNATest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Check for empty input data
        if len(data) == 0:
            return -1, False
        
        if not isinstance(data, (str)) or len(data) < 10:
            return -1, False
        
        n = len(data)
        subsequence_count = {}  # Dictionary to count occurrences of each subsequence
        
        # Extract subsequences of length 10
        for i in range(n - 9):
            subseq = data[i:i + 10]  # Get the substring of length 10
            if subseq in subsequence_count:
                subsequence_count[subseq] += 1
            else:
                subsequence_count[subseq] = 1
        
        observed = len(subsequence_count)  # Count of unique subsequences
        expected = 1024  # 2^10 = 1024 possible binary subsequences
        chi_square = ((observed - expected) ** 2) / expected
        
        # Calculate the p-value
        p_value = 1 - chi2.cdf(chi_square, 1023)  # 1024-1 = 1023 degrees of freedom
        
        if verbose:
            print(f"DNA Test - Chi-square: {chi_square}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)  # Return p-value and pass/fail result
