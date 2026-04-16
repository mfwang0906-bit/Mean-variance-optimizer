import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#pull stock historical data
tickers = ['TSM', 'INTC', 'META', 'NVDA', 'TSLA']
import datetime
data = yf.download(tickers, start='2023-01-01', end=datetime.date.today().strftime('%Y-%m-%d'))['Close']
returns = data.pct_change().dropna()

#calculate returns based on 252 trading days in a year
mean_returns = returns.mean() * 252
#calculate covariance matrix to represent variability
cov_matrix = returns.cov() * 252

# Monte Carlo 
num_portfolios = 10000
num_assets = len(tickers)
risk_free_rate = 0.04
results = np.zeros((3, num_portfolios))
weights_record = []

for i in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    weights_record.append(weights)
    port_return = np.dot(weights, mean_returns)
    port_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = (port_return - risk_free_rate) / port_volatility
    results[0, i] = port_return
    results[1, i] = port_volatility
    results[2, i] = sharpe

#Plotting a graph
results_df = pd.DataFrame(results.T, columns=['Return', 'Volatility', 'Sharpe'])
max_sharpe_idx = results_df['Sharpe'].idxmax()
min_vol_idx = results_df['Volatility'].idxmin()

plt.figure(figsize=(12, 7))
plt.scatter(results_df['Volatility'], results_df['Return'],
            c=results_df['Sharpe'], cmap='viridis', alpha=0.5, s=10)
plt.colorbar(label='Sharpe Ratio')
plt.scatter(results_df.loc[max_sharpe_idx, 'Volatility'],
            results_df.loc[max_sharpe_idx, 'Return'],
            color='red', marker='*', s=300, label='Max Sharpe')
plt.scatter(results_df.loc[min_vol_idx, 'Volatility'],
            results_df.loc[min_vol_idx, 'Return'],
            color='blue', marker='*', s=300, label='Min Volatility')
plt.xlabel('Annual Volatility')
plt.ylabel('Annual Return')
plt.title('Portfolio allocation')
plt.legend()
plt.show()

#giving summarized output
print("\nMax Sharpe Portfolio Weights:")
for ticker, weight in zip(tickers, weights_record[max_sharpe_idx]):
    print(f"  {ticker}: {weight:.1%}")