import pandas as pd
df=pd.read_csv("data.csv")
print("Initial Data")
print(df.head())

df=df.drop_duplicates()
print("\n After Removing Duplicates:")
print(df.head())

df["Customer_Name"]=df["Customer_Name"].fillna("Unknown")
df["Quantity"]=df["Quantity"].fillna(df["Quantity"].median())
df["Price"]=df["Price"].fillna(df["Price"].median())
print("\n After handling missing values:")

print("\n Data Summary (Numeric Stats):")
print(df.describe())

print("\n Product Counts:")
print(df["Product"].value_counts)

df.to_csv("data_cleaned.csv", index=False)
print("\n Cleaned data saved as data_cleaned.csv") 

import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
df["Product"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Product wise order count")
plt.xlabel("Product")
plt.ylabel("Number of orders")
plt.tight_layout()
plt.savefig("product_count.png")
plt.show()

plt.figure(figsize=(6,4))
df["Quantity"].plot(kind="hist",bins=5, color="lightgreen")
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("quantity_hist_png")
plt.show

plt.figure(figsize=(6,4))
df["Price"].plot(kind="hist", bins=5, color="salmon")
plt.title("Price distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_hist.png")
plt.show()
