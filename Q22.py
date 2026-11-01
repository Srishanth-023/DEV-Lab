# Question 22: Use Pandas melt() to convert a dataset from wide format to long format, and produce a grouped chart to display the converted data.
# Q22: melt() wide -> long and grouped chart
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ---- Small monthly passengers dataset (1958-1960) ----
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
flights = pd.DataFrame({
    "year": np.repeat([1958, 1959, 1960], 12),
    "month": months * 3,
    "passengers": [
        340, 318, 362, 348, 363, 435, 491, 505, 404, 359, 310, 337,
        360, 342, 406, 396, 420, 472, 548, 559, 463, 407, 362, 405,
        417, 391, 419, 461, 472, 535, 622, 606, 508, 461, 390, 432,
    ],
})

wide = flights.pivot(index="year", columns="month", values="passengers")
wide = wide[months].reset_index()
print("Wide format:")
print(wide)

long = wide.melt(id_vars="year", var_name="month", value_name="passengers")
print("\nLong format:")
print(long.head())

sns.barplot(data=long, x="month", y="passengers", hue="year", palette="Set2")
plt.title("Monthly Passengers 1958-1960")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.legend(title="Year")
plt.show()
