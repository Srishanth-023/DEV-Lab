# Question 4: Use Pandas pivot() to convert a long-format dataset into wide format, and construct a line chart to display changes across categories.
# Q4: pivot() long -> wide format and line chart
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

print("Long format:")
print(flights.head())

wide = flights.pivot(index="month", columns="year", values="passengers")
wide = wide.reindex(months)
print("\nWide format:")
print(wide)

wide.plot(marker="o", figsize=(9, 5))
plt.title("Monthly Passengers across Years")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.legend(title="Year")
plt.grid(alpha=0.3)
plt.show()
