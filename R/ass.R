library(reshape2)
library(quantmod)
library(ggplot2)
library(tidyverse)
library(gridExtra)
library(tseries)
library(forecast)

plot_arch_process <- function(n, a0, a) {
  set.seed(14)
  p <- length(a)
  eps <- numeric(n)
  h <- numeric(n)
  z <- rnorm(n)
  
  h[1:p] <- a0 / (1 - sum(a))
  eps[1:p] <- sqrt(h[1:p]) * z[1:p]
  
  for (t in (p + 1):n) {
    h[t] <- a0 + sum(a * eps[(t - 1):(t - p)]^2)
    eps[t] <- sqrt(h[t]) * z[t]
  }
  
  sim_data <- data.frame(time = 1:n, eps = eps, sigma2 = h)
  
  p1 <- ggplot(sim_data, aes(x = time, y = eps)) +
    geom_line(color = "navy") +
    labs(title = "Simulated ARCH Process", x = "Time", y = expression(epsilon[t])) +
    theme_minimal(base_size = 14)
  
  p2 <- ggplot(sim_data, aes(x = time, y = sigma2)) +
    geom_line(color = "brown") +
    labs(title = "Conditional Variance", x = "Time", y = expression(sigma[t]^2)) +
    theme_minimal(base_size = 14)
  
  grid.arrange(p1, p2, ncol = 2)
}

plot_arch_process(n = 500, a0 = 0.1, a = c(0.5))
plot_arch_process(n=500, a0 = 0.1, a = c(0.2, 0.1, 0.1, 0.1, 0.3))


steepest_ascent_fit <- function(data,
                                lr = 1e-4,
                                step = 1e-4,
                                tol = 1e-6,
                                max_iter = 5000,
                                verbose = FALSE) {
  
  T_len <- length(data)
  beta0_current <- 0
  beta1_current <- 0
  beta0_new <- 0
  beta1_new <- 0
  
  for (iter in 1:max_iter) {
    errors <- data[2:T_len] - beta0_current - beta1_current * data[1:(T_len - 1)]
    
    grad0 <- sum(errors)
    grad1 <- sum(errors * data[1:(T_len - 1)])
    
    beta0_new <- beta0_current + step * grad0
    beta1_new <- beta1_current + step * grad1
    
    grad_norm <- sqrt((beta0_new-beta0_current)^2 + (beta1_new-beta1_current)^2)
    if (grad_norm < tol) {
      if (verbose) message("Converged in ", iter, " iterations; gradient norm = ", signif(grad_norm, 3))
      break
    }
    
    beta0_current = beta0_new
    beta1_current = beta1_new
    
    if (verbose && iter %% 500 == 0) {
      message("Iteration ", iter, ": beta0 = ", round(beta0_current, 4),
              ", beta1 = ", round(beta1_current, 4),
              ", grad_norm = ", signif(grad_norm, 3))
    }
  }
  
  list(beta0 = beta0_current,
       beta1 = beta1_current,
       iterations = iter,
       grad_norm = grad_norm)
}

set.seed(14)
n <- 500
x <- numeric(n)
x[1] <- 0
for (i in 2:n) {
  x[i] <- 0.2 + 0.5*x[i-1] + rnorm(1)
}

# estimate
mle_est <- steepest_ascent_fit(x, lr=1e-4, tol=1e-5, max_iter=5000, verbose=TRUE)
print(mle_est)


library(quantmod)

tesla_data <- getSymbols("TSLA", src="yahoo",
                        from = "2010-07-01",
                        to   = "2014-12-31",
                        auto.assign = FALSE)
prices    <- Cl(tesla_data)
log_prices <- log(prices)

price_df <- data.frame(
  date = index(prices),
  price = as.numeric(prices),
  log_price = as.numeric(log_prices)
)

p1 <- ggplot(price_df, aes(x = date, y = price)) +
  geom_line(color = "navy", size = 1) +
  labs(title = "TESLA Stock Prices (2010–2014)",
       x = "Date", y = "Price (USD)") +
  theme_minimal(base_size = 14) +
  theme(plot.title = element_text(face = "bold", size = 16, hjust = 0.5))

p2 <- ggplot(price_df, aes(x = date, y = log_price)) +
  geom_line(color = "brown", size = 1) +
  labs(title = "Log-Transformed TESLA Prices (2010–20014)",
       x = "Date", y = "Log(Price)") +
  theme_minimal(base_size = 14) +
  theme(plot.title = element_text(face = "bold", size = 16, hjust = 0.5))


grid.arrange(p1, p2, ncol = 1)

time_idx <- 1:nrow(price_df)
trend_mod <- lm(log_price ~ time_idx, data = price_df)
price_df$detrended <- resid(trend_mod)

adf.test(price_df$detrended)


log_returns <- diff(log_prices)
log_returns_df <- data.frame(time = time(log_returns), value = as.numeric(log_returns))

# Plot log returns
ggplot(log_returns_df, aes(x = time, y = value)) +
  geom_line(color = "navy", size = 1) +
  labs(title = "Log Returns of TESLA Stock Data (2010–2014)",
       x = "Date", y = "Return") +
  theme_minimal(base_size = 14) +
  theme(plot.title = element_text(face = "bold", size = 16, hjust = 0.5))


# Rolling forecast
n_obs <- length(log_returns)
train_cutoff <- floor(0.7 * n_obs)
future_actual <- log_returns[(train_cutoff + 1):n_obs]
forecast_vals <- numeric(length(future_actual))
ci_lower <- numeric(length(future_actual))
ci_upper <- numeric(length(future_actual))

# One-step rolling forecast with 95% confidence interval
for (j in seq_along(future_actual)) {
  print(j)
  training_subset <- log_returns[1:(train_cutoff + j - 1)]
  model_fit <- auto.arima(training_subset)
  fc_result <- forecast(model_fit, h = 1, level = c(95))
  
  forecast_vals[j] <- fc_result$mean
  ci_lower[j] <- fc_result$lower[1]
  ci_upper[j] <- fc_result$upper[1]
}

forecast_df <- data.frame(
  date = index(log_prices)[(train_cutoff + 1):n_obs],
  actual = as.numeric(future_actual),
  forecast = forecast_vals,
  lower_bound = ci_lower,
  upper_bound = ci_upper
)

# Plot forecast results
ggplot(forecast_df, aes(x = date)) +
  geom_line(aes(y = actual, color = "Actual"), size = 1) +
  geom_line(aes(y = forecast, color = "Forecast"), size = 1) +
  geom_ribbon(aes(ymin = lower_bound, ymax = upper_bound), fill = "gray", alpha = 0.5) +
  labs(title = "One-Step Rolling Forecast with 95% Confidence Intervals (TESLA Log Returns)",
       y = "Log Return", x = "Date", color = "Series") +
  scale_color_manual(values = c("Actual" = "navy", "Forecast" = "brown")) +
  theme_minimal(base_size = 14) +
  theme(plot.title = element_text(face = "bold", size = 16, hjust = 0.5))