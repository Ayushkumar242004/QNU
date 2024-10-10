class SqueezeTest:
    @staticmethod
    def SqueezeTest(data, verbose=False):
        k = len(data)
        products = np.cumprod(data)
        squeezed = np.sum(products < 1e-10)  # Check if product becomes too small
        
        expected = k * 1e-10
        variance = expected * (1 - expected)
        z_statistic = (squeezed - expected) / np.sqrt(variance)
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        
        if verbose:
            print(f"Squeeze Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        return p_value, (p_value >= 0.01)
