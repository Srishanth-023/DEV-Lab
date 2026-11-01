# Question 10: Organize categorical frequencies in descending order and produce a Pareto chart with a cumulative-percentage line.
# Q10: Pareto chart (descending bars + cumulative % line)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---- Small dataset: defect types recorded in a factory (60 records) ----
defects = pd.Series(
    ["Scratch"] * 22 + ["Dent"] * 14 + ["Crack"] * 9 + ["Paint"] * 7
    + ["Rust"] * 5 + ["Other"] * 3
)

counts = defects.value_counts()                     # descending order
cum_pct = counts.cumsum() / counts.sum() * 100
print(pd.DataFrame({"count": counts, "cum_%": cum_pct.round(1)}))

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(counts.index, counts.values, color="steelblue")
ax.set_xlabel("Defect type")
ax.set_ylabel("Frequency")
ax.set_title("Pareto Chart of Defects")

ax2 = ax.twinx()
ax2.plot(counts.index, cum_pct.values, "r-o")
ax2.axhline(80, color="gray", linestyle="--")
ax2.set_ylabel("Cumulative percentage")
ax2.set_ylim(0, 105)

plt.tight_layout()
plt.show()
