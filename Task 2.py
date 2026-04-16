import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Customer_ID': list(range(1,11)),
    'Subscription_Months': [12,2,10,11,3,9,13,1,14,8],
    'Monthly_Charges': [500,700,600,550,750,620,540,900,520,610],
    'Churn': ['No','Yes','No','No','Yes','No','No','Yes','No','No']
}

df = pd.DataFrame(data)

# -------- Basic Analysis --------
print("Total Customers:", len(df))
print("Churn Customers:", df['Churn'].value_counts()['Yes'])

# -------- Graph 1: Bar Chart --------
counts = df['Churn'].value_counts()

plt.figure()
bars = plt.bar(counts.index, counts.values)

# Add values on top
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + 0.25, y, y)

plt.title("Churn vs Retained Customers")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")
plt.grid(axis='y')
plt.show()

# -------- Graph 2: Line Chart --------
plt.figure()

# Line with markers
plt.plot(df['Subscription_Months'], marker='o')

# Average line
avg = df['Subscription_Months'].mean()
plt.axhline(avg, linestyle='--')

plt.title("Subscription Months Trend")
plt.xlabel("Customer Index")
plt.ylabel("Months")
plt.grid()

plt.show()
