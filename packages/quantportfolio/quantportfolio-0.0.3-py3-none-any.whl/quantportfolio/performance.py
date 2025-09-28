import numpy as np

def portfolio_performance(weights, mean_returns, cov_matrix, rf):
    """
    Given portfolio weights, compute expected return, volatility, and Sharpe ratio.
    :param weights: array of portfolio weights
    :param mean_returns: expected returns of assets
    :param cov_matrix: covariance matrix of assets
    :param rf: risk-free rate
    """
    port_return = np.dot(weights, mean_returns)
    port_vol = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = (port_return - rf) / port_vol
    return port_return, port_vol, sharpe
