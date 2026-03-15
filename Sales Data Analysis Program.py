import pandas as pd

# Sales dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "City": ["Chennai", "Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai"],
    "Sales": [50000, 30000, 20000, 45000, 35000, 25000]
}

df = pd.DataFrame(data)

print("Sales Data")
print(df)
print()

# Total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
print()

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()

print("Sales by Product")
print(product_sales)
print()

# Sales by city
city_sales = df.groupby("City")["Sales"].sum()

print("Sales by City")
print(city_sales)
print()

# Highest sale
highest = df.loc[df["Sales"].idxmax()]

print("Highest Sale Record")
print(highest)