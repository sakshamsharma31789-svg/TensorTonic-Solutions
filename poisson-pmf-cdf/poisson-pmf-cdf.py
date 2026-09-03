import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    current_pmf = math.exp(-lam)
    cds = current_pmf
    for i in range(1,k+1):
        current_pmf *=lam/i
        cds += current_pmf
    return {
        'pmf':float(current_pmf),
        'cdf':float(cds)
    }
    
    pass