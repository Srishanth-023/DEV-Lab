# Question 13: Load a real-world dataset using Pandas and apply data-quality preprocessing techniques to identify missing values, duplicate records, inconsistent data types, and categorical variables, then clean the dataset using suitable methods.
# Q13: Data-quality checks and cleaning
import numpy as np
import pandas as pd

# ---- Small messy dataset (use pd.read_csv("file.csv") for a real file) ----
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 4, 5, 6, 7],
    "name": ["Ann", "Bob", "Cara", "Dev", "Dev", "Eli", "Fay", "Gus"],
    "age": [25, np.nan, 31, 40, 40, "29", np.nan, 52],      # mixed types
    "city": ["Chennai", "Madurai", None, "Chennai", "Chennai",
             "Salem", "Madurai", "Chennai"],
    "salary": [50000, 42000, 61000, np.nan, np.nan, 45000, 52000, 90000],
})

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate records:", df.duplicated().sum())
cat_cols = df.select_dtypes(include="object").columns.tolist()
print("Categorical (object) columns:", cat_cols)

# ---- Cleaning ----
df = df.drop_duplicates()
df["age"] = pd.to_numeric(df["age"])                      # fix data type
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["city"] = df["city"].fillna(df["city"].mode()[0])
df["city"] = df["city"].astype("category")

print("\nAfter cleaning:")
print(df)
print("Missing:", df.isna().sum().sum(), "| Duplicates:", df.duplicated().sum())
print(df.dtypes)
