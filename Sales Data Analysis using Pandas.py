import pandas as pd

# Step 1: Create dataset
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
    "Quantity": [2, 5, 3, 4, 6],
    "Price": [50000, 20000, 50000, 30000, 20000]
}

df = pd.DataFrame(data)

# Step 2: Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Step 3: Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Step 4: Total Revenue
total_revenue = df["Revenue"].sum()

# Step 5: Best Selling Product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Step 6: Highest Sales Day
best_day = df.groupby("Date")["Revenue"].sum().idxmax()

# Step 7: Output
print("Sales Data:\n", df)
print("\nTotal Revenue:", total_revenue)
print("Best Selling Product:", best_product)
print("Highest Revenue Day:", best_day)