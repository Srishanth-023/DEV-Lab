# Question 16: Apply a logarithmic scale to a suitable axis and produce plots using both linear and logarithmic scales to display highly skewed numerical data.
# Q16: Linear vs logarithmic scale for highly skewed data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- Small skewed dataset: 100 log-normal incomes ----
np.random.seed(1)
income = np.sort(np.random.lognormal(mean=10, sigma=1.2, size=100))
print("Skewness:", round(pd.Series(income).skew(), 2))

fig, ax = plt.subplots(2, 2, figsize=(11, 8))

ax[0, 0].hist(income, bins=20, edgecolor="black")
ax[0, 0].set(title="Histogram - linear scale", xlabel="Income",
             ylabel="Frequency")

log_bins = np.logspace(np.log10(income.min()), np.log10(income.max()), 20)
ax[0, 1].hist(income, bins=log_bins, edgecolor="black")
ax[0, 1].set_xscale("log")
ax[0, 1].set(title="Histogram - logarithmic x-axis", xlabel="Income (log)",
             ylabel="Frequency")

ax[1, 0].plot(income, marker="o", markersize=3)
ax[1, 0].set(title="Sorted values - linear y-axis", xlabel="Rank",
             ylabel="Income")

ax[1, 1].plot(income, marker="o", markersize=3)
ax[1, 1].set_yscale("log")
ax[1, 1].set(title="Sorted values - logarithmic y-axis", xlabel="Rank",
             ylabel="Income (log)")

plt.tight_layout()
plt.show()
