import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip first 4 rows)
df = pd.read_csv("world_population.csv", skiprows=4)

# Check columns
print(df.head())

# ---------------------------
# Histogram (latest year data)
# ---------------------------
plt.figure()
plt.hist(df['2022'], bins=10)
plt.title("Population Distribution (2022)")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.savefig("population_histogram.png")
plt.show()

# ---------------------------
# Bar Chart (Top 10 Countries)
# ---------------------------
top10 = df.sort_values(by='2022', ascending=False).head(10)

plt.figure()
plt.bar(top10['Country Name'], top10['2022'])
plt.title("Top 10 Countries by Population (2022)")
plt.xticks(rotation=45)
plt.savefig("top10_population.png")
plt.show()

print("✅ Task 1 with real dataset completed!")