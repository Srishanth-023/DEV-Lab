# Question 19: Given an unseen real-world dataset, apply Python and Pandas operations to display the dataset dimensions, data types, summary statistics, missing values, and duplicate records, and perform suitable data-cleaning operations.
# Q19: Unseen dataset - dimensions, types, summary, missing, duplicates, cleaning
import numpy as np
import pandas as pd

# ---- Small employee dataset (use pd.read_csv("file.csv") for a real file) ----
df = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 105, 106, 107, 108],
    "dept": ["IT", "HR", "IT", None, "Sales", "Sales", "HR", "IT", "Sales"],
    "experience": [5, 3, np.nan, 8, 2, 2, 10, 4, np.nan],
    "salary": [60000, 45000, 58000, 75000, np.nan, np.nan, 82000, 52000, 48000],
    "rating": ["4", "3", "5", "4", "3", "3", "5", "4", "2"],     # stored as text
})

print("Dimensions:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe(include="all").T)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate records:", df.duplicated().sum())

# ---- Cleaning ----
df = df.drop_duplicates()
df["rating"] = pd.to_numeric(df["rating"])
df["experience"] = df["experience"].fillna(df["experience"].median())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["dept"] = df["dept"].fillna(df["dept"].mode()[0])

print("\nCleaned shape:", df.shape)
print("Missing:", df.isna().sum().sum(), "| Duplicates:", df.duplicated().sum())
print(df)
