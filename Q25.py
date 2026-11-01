# Question 25: Use a suitable dataset to apply a scatter plot and calculate Pearson's correlation coefficient for two numerical variables, then report the direction and strength indicated by the results.
# Q25: Scatter plot and Pearson correlation coefficient
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr

# ---- Small restaurant dataset (30 records) ----
tips = pd.DataFrame({
    "total_bill": [
        16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78,
        10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65,
        17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.70, 19.65,
    ],
    "tip": [
        1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23,
        1.71, 5.00, 1.57, 3.00, 3.02, 3.92, 1.67, 3.71, 3.50, 3.35,
        4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.00, 2.00, 4.30, 3.00,
    ],
    "sex": ["Male", "Female", "Female"] * 10,
    "smoker": ["No", "No", "Yes", "No", "Yes"] * 6,
    "day": ["Thur", "Fri", "Sat", "Sun"] * 7 + ["Sat", "Sun"],
    "size": [
        2, 3, 3, 2, 4, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2,
        4, 3, 3, 3, 3, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2,
    ],
})
tips["time"] = np.where(tips["day"].isin(["Sat", "Sun"]), "Dinner", "Lunch")
days = ["Thur", "Fri", "Sat", "Sun"]
tips["day"] = pd.Categorical(tips["day"], categories=days, ordered=True)

r, p = pearsonr(tips["total_bill"], tips["tip"])

plt.scatter(tips["total_bill"], tips["tip"])
plt.title(f"Total Bill vs Tip (r = {r:.2f})")
plt.xlabel("Total bill")
plt.ylabel("Tip")
plt.show()

if abs(r) >= 0.7:
    strength = "strong"
elif abs(r) >= 0.4:
    strength = "moderate"
else:
    strength = "weak"
direction = "positive" if r > 0 else "negative"
print(f"Pearson r = {r:.3f} (p-value = {p:.2e})")
print(f"Result: {strength} {direction} linear relationship.")
