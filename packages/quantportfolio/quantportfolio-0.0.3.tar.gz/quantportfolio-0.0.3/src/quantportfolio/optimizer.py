import numpy as np
from scipy.optimize import minimize
from performance import portfolio_performance

def negative_sharpe(weights, mean_returns, cov_matrix, rf):
    """Objective function: negative Sharpe ratio (to be minimized)."""
    return -portfolio_performance(weights, mean_returns, cov_matrix, rf)[2]

def max_sharpe_ratio(mean_returns, cov_matrix, rf, bounds=None):
    """
    Find the portfolio weights that maximize the Sharpe ratio.
    :param mean_returns: expected returns of assets
    :param cov_matrix: covariance matrix of assets
    :param rf: risk-free rate
    :param bounds: optional bounds for weights
    """
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, rf)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    if bounds is None:
        bounds = tuple((0, 1) for _ in range(num_assets))  # default: long-only
    result = minimize(negative_sharpe,
                      num_assets*[1./num_assets,],  # initial equal weights
                      args=args,
                      method='SLSQP',
                      bounds=bounds,
                      constraints=constraints)
    return result
