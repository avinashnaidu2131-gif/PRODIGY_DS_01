# PRODIGY_DS_01 - Task 1 (No seaborn)

import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = pd.DataFrame({
    'Age': [18,22,25,30,35,40,22,25,30,28,32,36,45,50,23,27],
    'Gender': ['Male','Female','Male','Female','Male','Female',
               'Male','Female','Male','Male','Female','Female',
               'Male','Female','Male','Female']
})

# ---------------------------
# Histogram (Age)
# ---------------------------
plt.figure()
plt.hist(data['Age'], bins=6)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_histogram.png")
plt.show()

# ---------------------------
# Bar Chart (Gender)
# ---------------------------
plt.figure()
data['Gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_bar_chart.png")
plt.show()

print("✅ Task 1 Completed Successfully")