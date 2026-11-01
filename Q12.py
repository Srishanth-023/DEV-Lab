# Question 12: Organize numerical observations into class intervals, calculate their frequencies, and produce a frequency polygon.
# Q12: Class intervals, frequencies and frequency polygon
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

bins = np.arange(5, 50, 5)                        # 5-10, 10-15, ... 40-45
freq = pd.cut(tips["total_bill"], bins=bins).value_counts().sort_index()
print(freq)

mid = (bins[:-1] + bins[1:]) / 2                  # class mid-points
mid = np.r_[mid[0] - 5, mid, mid[-1] + 5]         # add empty classes at ends
y = np.r_[0, freq.values, 0]

plt.plot(mid, y, marker="o")
plt.title("Frequency Polygon of Total Bill")
plt.xlabel("Class mid-point")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.show()
