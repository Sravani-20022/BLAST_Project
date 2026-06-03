import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel(r"D:\BLAST\report\results.txt.xlsx")

# Select top 10 hits
top_hits = df.head(10)

# Print important columns
print("\nTop 10 BLAST Hits\n")
print(top_hits[["Scientific name", "Per identity", "Query Cover"]])

# Create bar chart
plt.figure(figsize=(10,5))
plt.bar(top_hits["Scientific name"], top_hits["Per identity"])

plt.xticks(rotation=45, ha="right")
plt.xlabel("Species")
plt.ylabel("Percent Identity")
plt.title("BLAST Sequence Similarity of SUMM2 Gene")

plt.tight_layout()
plt.show()
