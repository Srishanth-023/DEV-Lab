# Question 40: Use Matplotlib or Seaborn to produce density and contour plots for two numerical variables in a suitable dataset.
# Q40: Density and contour plots for two numerical variables
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ---- Small iris-type dataset (30 records) ----
iris = pd.DataFrame({
    "sepal_length": [
        5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
        7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2,
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
    ],
    "sepal_width": [
        3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1,
        3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7,
        3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6,
    ],
    "petal_length": [
        1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5,
        4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 3.3, 4.6, 3.9,
        6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1,
    ],
    "petal_width": [
        0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1,
        1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4,
        2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5,
    ],
    "species": np.repeat(["setosa", "versicolor", "virginica"], 10),
})

fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))

sns.kdeplot(data=iris, x="sepal_length", fill=True, ax=ax[0])
ax[0].set_title("1-D Density Plot")

sns.kdeplot(data=iris, x="sepal_length", y="petal_length",
            fill=True, cmap="Blues", ax=ax[1])
ax[1].set_title("2-D Density Plot (filled)")

sns.kdeplot(data=iris, x="sepal_length", y="petal_length",
            levels=8, color="black", ax=ax[2])
ax[2].set_title("Contour Plot")

plt.tight_layout()
plt.show()
