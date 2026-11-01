# Question 15: Given a dataset containing two categorical variables, use Pandas to generate a two-way contingency table and create a suitable visualization to display their relationship.
# Q15: Two-way contingency table and visualization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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

table = pd.crosstab(tips["day"], tips["smoker"])
print("Contingency table:")
print(pd.crosstab(tips["day"], tips["smoker"], margins=True))
print("\nRow percentages:")
print(pd.crosstab(tips["day"], tips["smoker"], normalize="index").round(2))

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
table.plot(kind="bar", ax=ax[0])
ax[0].set_title("Day vs Smoker (grouped bars)")
ax[0].set_xlabel("Day")
ax[0].set_ylabel("Count")

sns.heatmap(table, annot=True, fmt="d", cmap="Blues", ax=ax[1])
ax[1].set_title("Day vs Smoker (heatmap)")
plt.tight_layout()
plt.show()
