import pandas as pd

# Create student dataset
data = {
    "Name": ["Arun", "Priya", "Rahul", "Sneha", "Kiran"],
    "Math": [85, 90, 78, 92, 88],
    "Science": [88, 76, 85, 91, 79],
    "English": [90, 89, 84, 95, 86]
}

df = pd.DataFrame(data)

print("Student Data")
print(df)
print()

# Calculate total
df["Total"] = df["Math"] + df["Science"] + df["English"]

# Calculate average
df["Average"] = df["Total"] / 3

print("Data with Total and Average")
print(df)
print()

# Find top student
top_student = df.loc[df["Total"].idxmax()]

print("Top Student")
print(top_student)
print()

# Students scoring above 85 average
high_scores = df[df["Average"] > 85]

print("Students with Average > 85")
print(high_scores)