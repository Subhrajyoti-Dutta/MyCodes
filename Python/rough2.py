import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

sns.set(style='whitegrid', font_scale=1.2)

# 1️⃣ Simulate ARCH process and plot
def plot_arch_process(n, a0, a):
    np.random.seed(14)
    p = len(a)
    eps = np.zeros(n)
    h = np.zeros(n)
    z = np.random.normal(size=n)

    h[:p] = a0 / (1 - sum(a))
    eps[:p] = np.sqrt(h[:p]) * z[:p]

    for t in range(p, n):
        h[t] = a0 + np.sum(np.array(a) * eps[(t - p):t]**2)
        eps[t] = np.sqrt(h[t]) * z[t]

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    axes[0].plot(range(n), eps, color='navy')
    axes[0].set_title('Simulated ARCH Process')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel(r'$\epsilon_t$')

    axes[1].plot(range(n), h, color='brown')
    axes[1].set_title('Conditional Variance')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel(r'$\sigma_t^2$')

    plt.tight_layout()
    plt.show()

plot_arch_process(n=500, a0=0.1, a=[0.5])
plot_arch_process(n=500, a0=0.1, a=[0.2, 0.1, 0.1, 0.1, 0.3])

# 2️⃣ Steepest ascent fit for AR(1) model
def steepest_ascent_fit(data, step=1e-4, tol=1e-6, max_iter=5000, verbose=False):
    T_len = len(data)
    beta0_current = 0
    beta1_current = 0

    for iter in range(1, max_iter + 1):
        errors = data[1:] - beta0_current - beta1_current * data[:-1]

        grad0 = np.sum(errors)
        grad1 = np.sum(errors * data[:-1])

        beta0_new = beta0_current + step * grad0
        beta1_new = beta1_current + step * grad1

        grad_norm = np.sqrt((beta0_new - beta0_current)**2 + (beta1_new - beta1_current)**2)
        if grad_norm < tol:
            if verbose:
                print(f"Converged in {iter} iterations; gradient norm = {grad_norm:.5f}")
            break

        beta0_current = beta0_new
        beta1_current = beta1_new

        if verbose and iter % 500 == 0:
            print(f"Iteration {iter}: beta0 = {beta0_current:.4f}, beta1 = {beta1_current:.4f}, grad_norm = {grad_norm:.5f}")

    return {'beta0': beta0_current, 'beta1': beta1_current, 'iterations': iter, 'grad_norm': grad_norm}

# Generate synthetic AR(1) process
np.random.seed(14)
n = 500
x = np.zeros(n)
for i in range(1, n):
    x[i] = 0.2 + 0.5 * x[i - 1] + np.random.normal()

# Estimate parameters
mle_est = steepest_ascent_fit(x, step=1e-4, tol=1e-5, max_iter=5000, verbose=True)
print(mle_est)

# 3️⃣ Tesla stock data — download and plot
tesla_data = yf.download('TSLA', start='2010-07-01', end='2014-12-31')
prices = tesla_data['Close']
log_prices = np.log(prices)

price_df = pd.DataFrame({
    'date': prices.index,
    'price': prices.values,
    'log_price': log_prices.values
})

fig, axes = plt.subplots(2, 1, figsize=(14, 10))

axes[0].plot(price_df['date'], price_df['price'], color='navy')
axes[0].set_title('TESLA Stock Prices (2010–2014)', fontsize=16)
axes[0].set_ylabel('Price (USD)')

axes[1].plot(price_df['date'], price_df['log_price'], color='brown')
axes[1].set_title('Log-Transformed TESLA Prices (2010–2014)', fontsize=16)
axes[1].set_ylabel('Log(Price)')

plt.tight_layout()
plt.show()

# Detrend log prices
price_df['time_idx'] = np.arange(len(price_df))
trend_mod = np.polyfit(price_df['time_idx'], price_df['log_price'], 1)
trend_line = np.polyval(trend_mod, price_df['time_idx'])
price_df['detrended'] = price_df['log_price'] - trend_line

# ADF test on detrended series
adf_result = adfuller(price_df['detrended'])
print('ADF Statistic:', adf_result[0])
print('p-value:', adf_result[1])

# Compute log returns
log_returns = log_prices.diff().dropna()
log_returns_df = pd.DataFrame({'time': log_returns.index, 'value': log_returns.values})

plt.figure(figsize=(14, 6))
plt.plot(log_returns_df['time'], log_returns_df['value'], color='navy')
plt.title('Log Returns of TESLA Stock Data (2010–2014)', fontsize=16)
plt.ylabel('Return')
plt.show()

# Rolling forecast
n_obs = len(log_returns)
train_cutoff = int(0.7 * n_obs)

future_actual = log_returns.iloc[train_cutoff:]
forecast_vals = []
ci_lower = []
ci_upper = []

dates = future_actual.index

for j in range(len(future_actual)):
    training_subset = log_returns.iloc[:train_cutoff + j]
    model_fit = ARIMA(training_subset, order=(1,0,0)).fit()
    forecast_result = model_fit.get_forecast(steps=1)
    forecast_mean = forecast_result.predicted_mean.iloc[0]
    conf_int = forecast_result.conf_int(alpha=0.05).iloc[0]

    forecast_vals.append(forecast_mean)
    ci_lower.append(conf_int[0])
    ci_upper.append(conf_int[1])

forecast_df = pd.DataFrame({
    'date': dates,
    'actual': future_actual.values,
    'forecast': forecast_vals,
    'lower_bound': ci_lower,
    'upper_bound': ci_upper
})

plt.figure(figsize=(14, 7))
plt.plot(forecast_df['date'], forecast_df['actual'], label='Actual', color='navy')
plt.plot(forecast_df['date'], forecast_df['forecast'], label='Forecast', color='brown')
plt.fill_between(forecast_df['date'], forecast_df['lower_bound'], forecast_df['upper_bound'], color='gray', alpha=0.3)
plt.title('One-Step Rolling Forecast with 95% CI (TESLA Log Returns)', fontsize=16)
plt.ylabel('Log Return')
plt.legend()
plt.show()
