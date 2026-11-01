# Question 3: Using a dataset containing numerical and categorical variables, apply Matplotlib to generate a line plot, scatter plot, histogram, box plot, bar chart, and pie chart, and state the observations from each visualization.
# Q3: Line, scatter, histogram, box, bar, pie + observations (Matplotlib)
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

fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# 1. Line plot
avg_tip = tips.groupby("size")["tip"].mean()
ax[0, 0].plot(avg_tip.index, avg_tip.values, marker="o")
ax[0, 0].set(title="Line: Average tip by party size",
             xlabel="Party size", ylabel="Average tip")

# 2. Scatter plot
ax[0, 1].scatter(tips["total_bill"], tips["tip"], alpha=0.7)
ax[0, 1].set(title="Scatter: Bill vs Tip", xlabel="Total bill", ylabel="Tip")

# 3. Histogram
ax[0, 2].hist(tips["total_bill"], bins=8, edgecolor="black")
ax[0, 2].set(title="Histogram: Total bill", xlabel="Total bill",
             ylabel="Frequency")

# 4. Box plot
data = [tips.loc[tips["day"] == d, "total_bill"] for d in days]
ax[1, 0].boxplot(data, labels=days)
ax[1, 0].set(title="Box: Bill by day", xlabel="Day", ylabel="Total bill")

# 5. Bar chart
tip_sum = tips.groupby("day", observed=True)["tip"].sum()
ax[1, 1].bar(days, tip_sum.values, color="orange")
ax[1, 1].set(title="Bar: Total tips by day", xlabel="Day", ylabel="Sum of tips")

# 6. Pie chart
sex = tips["sex"].value_counts()
ax[1, 2].pie(sex, labels=sex.index, autopct="%1.1f%%")
ax[1, 2].set_title("Pie: Customer gender share")

plt.tight_layout()
plt.show()

print("Observations:")
print(f"1. Line: average tip rises with party size "
      f"({avg_tip.iloc[0]:.2f} -> {avg_tip.iloc[-1]:.2f}).")
print(f"2. Scatter: positive relation between bill and tip "
      f"(r = {tips['total_bill'].corr(tips['tip']):.2f}).")
print(f"3. Histogram: right-skewed; mean {tips['total_bill'].mean():.1f} "
      f"> median {tips['total_bill'].median():.1f}.")
print(f"4. Box: highest median bill on "
      f"{tips.groupby('day', observed=True)['total_bill'].median().idxmax()}.")
print(f"5. Bar: most tips collected on {tip_sum.idxmax()}.")
print(f"6. Pie: {sex.idxmax()} customers form the larger share.")
