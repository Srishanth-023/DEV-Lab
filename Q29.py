# Question 29: Given a real-world dataset containing at least three variables, use Pandas to create a pivot table and Seaborn to generate a heatmap and grouped bar chart from the summarized data.
# Q29: Pivot table, heatmap and grouped bar chart
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

pt = tips.pivot_table(values="tip", index="day", columns="sex",
                      aggfunc="mean", observed=True)
print(pt.round(2))

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(pt, annot=True, fmt=".2f", cmap="YlGnBu", ax=ax[0])
ax[0].set_title("Average Tip: Day x Sex")

long = pt.reset_index().melt(id_vars="day", value_name="avg_tip")
sns.barplot(data=long, x="day", y="avg_tip", hue="sex", ax=ax[1])
ax[1].set_title("Grouped Bar Chart: Average Tip")
ax[1].set_xlabel("Day")
ax[1].set_ylabel("Average tip")
plt.tight_layout()
plt.show()
