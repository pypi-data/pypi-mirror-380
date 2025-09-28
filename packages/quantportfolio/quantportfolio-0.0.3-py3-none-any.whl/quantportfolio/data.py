import yfinance as yf
import pandas as pd
import datetime

def get_stock_df(ticker, start="2024-01-01"):
    """Download single stock prices and compute daily returns"""
    end = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start, end=end)
    df = data[['Close']].reset_index()
    df.columns = ['Date', 'Price']
    df['return'] = df['Price'].pct_change()
    df.fillna(0, inplace=True)
    return df[['Date', 'return']].rename(columns={'return': f'return_{ticker}'})

def get_portfolio_returns(tickers, start="2024-01-01"):
    """Merge daily returns of multiple stocks into one DataFrame"""
    dfs = [get_stock_df(t, start=start) for t in tickers]
    df = dfs[0]
    for i in range(1, len(dfs)):
        df = df.merge(dfs[i], on="Date", how="outer")
    df.sort_values("Date", inplace=True)
    df.fillna(0, inplace=True)
    return df
