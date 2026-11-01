# Question 39: Given a dataset containing numerical and categorical attributes, apply Pandas operations to load, inspect, slice, transform, and group the data, and generate a summary of the results.
# Q39: Load, inspect, slice, transform, group and summarize
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

df = tips                      # for a real file: df = pd.read_csv("file.csv")

# 1. Inspect
print("Shape:", df.shape)
print(df.dtypes)
print(df.head())
print(df.describe())

# 2. Slice
print("\nBills above 25:")
print(df.loc[df["total_bill"] > 25, ["total_bill", "tip", "day"]])
print("\nFirst 5 rows, first 3 columns:")
print(df.iloc[:5, :3])

# 3. Transform
df["tip_pct"] = (df["tip"] / df["total_bill"] * 100).round(1)
df["size_group"] = pd.cut(df["size"], [0, 2, 4], labels=["small", "large"])

# 4. Group
summary = df.groupby(["day", "sex"], observed=True).agg(
    avg_bill=("total_bill", "mean"),
    avg_tip_pct=("tip_pct", "mean"),
    visits=("tip", "count"),
).round(2)
print("\nGrouped summary:")
print(summary)

# 5. Result summary
print(f"\nHighest average bill: {summary['avg_bill'].idxmax()}")
print(f"Highest average tip %: {summary['avg_tip_pct'].idxmax()}")
