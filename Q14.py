# Question 14: Calculate cumulative totals and cumulative percentages for a dataset, and produce a line chart to represent the cumulative pattern.
# Q14: Cumulative totals, cumulative percentages and line chart
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

df = flights[["year", "month", "passengers"]].copy()
df["cum_total"] = df["passengers"].cumsum()
df["cum_pct"] = df["cum_total"] / df["passengers"].sum() * 100
print(df.round(1).head(12))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(len(df)), df["cum_total"], "b-o", markersize=3)
ax.set_title("Cumulative Passengers (Jan 1958 - Dec 1960)")
ax.set_xlabel("Month number")
ax.set_ylabel("Cumulative total", color="b")

ax2 = ax.twinx()
ax2.plot(range(len(df)), df["cum_pct"], "r--")
ax2.set_ylabel("Cumulative percentage", color="r")
plt.show()
