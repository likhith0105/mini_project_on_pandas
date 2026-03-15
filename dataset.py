import pandas as pd

# Step 1: Create student data
data = {
    "Name": ["Arun", "Priya", "Rahul", "Sneha"],
    "Math": [85, 90, 78, 92],
    "Science": [88, 76, 85, 91],
    "English": [90, 89, 84, 95]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)
print()

# Step 3: Calculate total marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

print("Data with Total Marks:")
print(df)
print()

# Step 4: Find top student
top_student = df.loc[df["Total"].idxmax()]

print("Top Student:")
print(top_student)
print()

# Step 5: Filter students with total > 260
high_scores = df[df["Total"] > 260]

print("Students with Total > 260:")
print(high_scores)
