# Question 28: Convert a date column to datetime format, organize the records chronologically, and produce a time-series plot of a selected measurement.
# Q28: Convert to datetime, sort chronologically, time-series plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- Small unordered dataset with dates stored as text ----
df = pd.DataFrame({
    "date": ["2024-03-05", "2024-01-10", "2024-02-14", "2024-01-25",
             "2024-04-01", "2024-02-02", "2024-03-20", "2024-04-18"],
    "temperature": [30.5, 27.1, 28.4, 27.9, 33.2, 27.8, 31.0, 34.5],
})
print("Before:", df["date"].dtype)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").set_index("date")
print("After:", df.index.dtype)
print(df)

df["temperature"].plot(marker="o", figsize=(9, 4))
plt.title("Temperature over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(alpha=0.3)
plt.show()
