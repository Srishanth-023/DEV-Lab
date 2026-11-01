# Question 21: Given an unseen real-world dataset, apply Pandas preprocessing techniques to identify numerical and categorical attributes, check for missing and duplicate values, handle missing values using suitable methods, and generate a statistical summary of the cleaned dataset.
# Q21: Numerical/categorical attributes, missing & duplicate values, summary
import numpy as np
import pandas as pd

# ---- Small student dataset (use pd.read_csv("file.csv") for a real file) ----
df = pd.DataFrame({
    "roll_no": [1, 2, 3, 4, 5, 5, 6, 7, 8],
    "gender": ["F", "M", "M", None, "F", "F", "M", "F", "M"],
    "branch": ["CSE", "ECE", "CSE", "IT", "IT", "IT", None, "CSE", "ECE"],
    "attendance": [92.5, 80.0, np.nan, 75.5, 88.0, 88.0, 69.0, np.nan, 95.0],
    "marks": [78, 65, 82, np.nan, 90, 90, 55, 73, np.nan],
})

num_cols = df.select_dtypes(include="number").columns.tolist()
cat_cols = df.select_dtypes(exclude="number").columns.tolist()
print("Numerical attributes:", num_cols)
print("Categorical attributes:", cat_cols)
print("\nMissing values:\n", df.isna().sum())
print("Duplicate records:", df.duplicated().sum())

# ---- Handling ----
df = df.drop_duplicates()
df[num_cols] = df[num_cols].fillna(df[num_cols].median())      # numeric -> median
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])                # categorical -> mode

print("\nRemaining missing values:", df.isna().sum().sum())
print("\nStatistical summary of cleaned data:")
print(df.describe(include="all").T)
