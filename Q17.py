# Question 17: Given a real-world dataset, apply Pandas and scikit-learn preprocessing techniques to handle missing values, encode categorical variables, scale features, split the data into training and testing sets, and apply PCA to transform the data into two components for visualization.
# Q17: Preprocessing (impute, encode, scale, split) + PCA to 2 components
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ---- Small dataset with missing values and categorical columns ----
df = pd.DataFrame({
    "age": [25, 32, 47, 51, np.nan, 23, 36, 29, 41, 55,
            np.nan, 38, 27, 45, 33, 60, 28, 35, 49, 31],
    "income": [30, 42, 80, 95, 60, 28, 55, np.nan, 72, 110,
               48, 65, 35, 85, 50, 120, 38, 58, 90, np.nan],
    "spend": [12, 20, 35, 40, 25, 10, 22, 18, 30, 50,
              19, 28, 14, 38, 21, 55, 15, 24, 42, 17],
    "gender": ["M", "F"] * 10,
    "city": ["Chennai", "Madurai", "Salem"] * 6 + ["Chennai", "Madurai"],
    "purchased": [0, 0, 1, 1, 0, 0, 1, 0, 1, 1,
                  0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
})

# 1. Missing values
num_cols = ["age", "income", "spend"]
df[num_cols] = SimpleImputer(strategy="median").fit_transform(df[num_cols])

# 2. Encode categorical variables
df = pd.get_dummies(df, columns=["gender", "city"], drop_first=True, dtype=int)

# 3. Split, 4. Scale (fit on training data only)
X = df.drop(columns="purchased")
y = df["purchased"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)

# 5. PCA to two components
pca = PCA(n_components=2).fit(X_train_s)
Z = pca.transform(X_train_s)
print("Train/Test shapes:", X_train.shape, X_test.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_.round(3))

plt.scatter(Z[:, 0], Z[:, 1], c=y_train, cmap="coolwarm", edgecolor="k")
plt.colorbar(label="Purchased")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA (2 components) of Training Data")
plt.show()
