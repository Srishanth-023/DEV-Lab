# Question 6: Construct a 2-by-2 subplot layout to display four visualizations of a dataset, and label each subplot with an appropriate title and axis labels.
# Q6: 2-by-2 subplot layout
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

fig, ax = plt.subplots(2, 2, figsize=(12, 9))

ax[0, 0].hist(tips["total_bill"], bins=8, color="teal", edgecolor="black")
ax[0, 0].set_title("Distribution of Total Bill")
ax[0, 0].set_xlabel("Total bill")
ax[0, 0].set_ylabel("Frequency")

ax[0, 1].scatter(tips["total_bill"], tips["tip"], color="crimson")
ax[0, 1].set_title("Total Bill vs Tip")
ax[0, 1].set_xlabel("Total bill")
ax[0, 1].set_ylabel("Tip")

sns.boxplot(data=tips, x="day", y="tip", ax=ax[1, 0])
ax[1, 0].set_title("Tip by Day")
ax[1, 0].set_xlabel("Day")
ax[1, 0].set_ylabel("Tip")

tips.groupby("time")["total_bill"].mean().plot.bar(ax=ax[1, 1], color="gray")
ax[1, 1].set_title("Average Bill by Meal Time")
ax[1, 1].set_xlabel("Meal time")
ax[1, 1].set_ylabel("Average bill")

plt.tight_layout()
plt.show()
