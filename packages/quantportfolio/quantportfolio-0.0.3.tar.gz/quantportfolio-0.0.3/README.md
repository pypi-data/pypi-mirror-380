# quantportfolio
A simple toolkit for portfolio optimization (Sharpe ratio, efficient frontier).

## Installation
```bash
pip install quantportfolio
```
## Example
```bash
from quantportfolio import get_portfolio_returns, max_sharpe_ratio, portfolio_performance

# Define stock pool
tickers = ["NVDA", "AMZN", "META"]

# Download returns
df = get_portfolio_returns(tickers, start="2024-01-01")

# Compute annualized mean returns & covariance
returns = df.drop(columns=["Date"])
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252
rf = 0.036  # risk-free rate

# Optimize for max Sharpe Ratio
result = max_sharpe_ratio(mean_returns.values, cov_matrix.values, rf)
weights = result.x

# Evaluate performance
port_return, port_vol, sharpe = portfolio_performance(
    weights, mean_returns.values, cov_matrix.values, rf
)

print("Weights:", dict(zip(tickers, weights.round(4))))
print(f"Expected Annual Return: {port_return:.2%}")
print(f"Expected Volatility: {port_vol:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")
```
## License
MIT License - see the [LICENSE](LICENSE) file for details.