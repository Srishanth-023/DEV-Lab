# Question 36: Use Matplotlib reference lines and annotations to illustrate a specified threshold or notable observation in a suitable chart.
# Q36: Reference lines and annotations
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

plt.figure(figsize=(10, 5))
plt.plot(series, marker="o", label="Passengers")
plt.axhline(500, color="red", linestyle="--", label="Threshold = 500")
plt.axvline(pd.Timestamp("1959-01-01"), color="green", linestyle=":",
            label="Start of 1959")
plt.annotate(f"Peak: {series.max()}",
             xy=(series.idxmax(), series.max()),
             xytext=(pd.Timestamp("1959-09-01"), series.max() - 40),
             arrowprops=dict(arrowstyle="->"))
plt.title("Monthly Passengers with Threshold and Peak")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.legend()
plt.show()
