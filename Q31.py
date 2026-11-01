# Question 31: Given a numerical dataset, use a histogram, box plot, and summary statistics to determine the distribution shape and detect potential outliers.
# Q31: Distribution shape and outlier detection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

x = tips["total_bill"]

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].hist(x, bins=8, edgecolor="black")
ax[0].set(title="Histogram", xlabel="Total bill", ylabel="Frequency")
ax[1].boxplot(x, vert=False)
ax[1].set(title="Box plot", xlabel="Total bill")
plt.tight_layout()
plt.show()

print(x.describe().round(2))
skew = x.skew()
if skew > 0.5:
    shape = "right-skewed"
elif skew < -0.5:
    shape = "left-skewed"
else:
    shape = "approximately symmetric"
print(f"\nSkewness = {skew:.2f} -> {shape}")

q1, q3 = x.quantile([0.25, 0.75])
iqr = q3 - q1
outliers = x[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]
print(f"Outlier limits: ({q1 - 1.5 * iqr:.2f}, {q3 + 1.5 * iqr:.2f})")
print("Potential outliers:", sorted(outliers.tolist()))
