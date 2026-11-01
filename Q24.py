# Question 24: Calculate a rolling mean for a time-series dataset and construct a plot showing both the original values and the moving-average trend.
# Q24: Rolling mean of a time series
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- Small monthly passengers dataset (1958-1960) ----
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
flights = pd.DataFrame({
    "year": np.repeat([1958, 1959, 1960], 12),
    "month": months * 3,
    "passengers": [
        340, 318, 362, 348, 363, 435, 491, 505, 404, 359, 310, 337,
        360, 342, 406, 396, 420, 472, 548, 559, 463, 407, 362, 405,
        417, 391, 419, 461, 472, 535, 622, 606, 508, 461, 390, 432,
    ],
})

dates = pd.date_range("1958-01-01", periods=len(flights), freq="MS")
series = pd.Series(flights["passengers"].values, index=dates)
rolling = series.rolling(window=6).mean()

plt.figure(figsize=(10, 5))
plt.plot(series, marker="o", label="Original")
plt.plot(rolling, color="red", linewidth=2, label="6-month rolling mean")
plt.title("Monthly Passengers with Moving Average")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
