import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df.head()
print(df.head())

print(df.isnull().sum())

df.fillna(0,inplace=True)

df["Date"]=pd.to_datetime(df["Date"])

print(df.info())

df["Total_sales"]=np.multiply(df["Units_Sold"],df["Unit_Price"])
df.head()
print(df.head()) 

print(df.head())
total_revenue = df["Total_sales"].sum()
avg_units = df.groupby("Product")["Units_Sold"].mean()
top_product = df.groupby("Product")["Total_sales"].sum().idxmax()

print(f"\nTotal Revenue: {total_revenue}")
print("\nAverage Units Sold per Product:\n", avg_units)
print(f"\nTop Selling Product: {top_product}")

                                       
                                       #NORMAL CHART 
plt.figure(figsize=(8,4))
plt.plot(df["Date"],df["Total_sales"],marker="o",color="grey")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total sales")
plt.grid(True)
plt.show()


                                     #BAR CHART
product_sales=df.groupby("Product")["Total_sales"].sum()
plt.figure(figsize=(6,4))
plt.bar(product_sales.index,product_sales.values,color=["black","skyblue","grey"])
plt.title("TOTAL SALES BY PRODUCT")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()

                                       #PIE CHART

import matplotlib.pyplot as plt
product_sales = df.groupby("Product")["Total_sales"].sum()
plt.figure(figsize=(6, 4))
plt.pie(product_sales.values, 
        labels=product_sales.index, 
        autopct='%1.1f%%', 
        colors=["blue", "skyblue", "grey"])
plt.title("Total Sales by Product")
plt.show()
