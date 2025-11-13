import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset (tab-separated)
df = pd.read_csv(r"C:\Users\kamaldeep\Documents\marketing_campaign.csv", sep="\t")

# 2. Fill missing Income values with median
df['Income'] = df['Income'].fillna(df['Income'].median())

# 3. Standardize text columns
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

# 4. Convert date column to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 7. Save cleaned dataset
df.to_csv(r"C:\Users\kamaldeep\Documents\marketing_campaign_cleaned.csv", index=False)

# 8. Inspect
print(df.info())
print(df.head())

# 9. Visualization

# Income distribution
plt.figure(figsize=(8,5))
sns.histplot(df['income'], bins=20, kde=True, color='skyblue')
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.show()

# Total spending per education
df['total_spent'] = df[['mntwines','mntfruits','mntmeatproducts','mntfishproducts','mntsweetproducts','mntgoldprods']].sum(axis=1)
plt.figure(figsize=(8,5))
sns.barplot(x='education', y='total_spent', data=df, palette='pastel')
plt.title("Average Total Spending by Education")
plt.ylabel("Average Spending")
plt.xticks(rotation=45)
plt.show()
