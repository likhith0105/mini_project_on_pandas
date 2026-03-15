import pandas as pd

# Step 1: Create employee dataset
data = {
    "Employee": ["Ravi", "Anita", "Kumar", "Divya", "Raj", "Meena", "Arjun"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
    "Salary": [60000, 45000, 70000, 65000, 48000, 72000, 69000],
    "Experience": [5, 3, 7, 6, 4, 8, 6]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

print("Employee Data")
print(df)
print()

# Step 3: Average salary
avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)
print()

# Step 4: Department-wise salary
dept_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary by Department")
print(dept_salary)
print()

# Step 5: Employees with more than 5 years experience
experienced_emp = df[df["Experience"] > 5]
print("Employees with Experience > 5 years")
print(experienced_emp)
print()

# Step 6: Highest paid employee
highest_paid = df.loc[df["Salary"].idxmax()]
print("Highest Paid Employee")
print(highest_paid)
print()

# Step 7: Sort employees by salary
sorted_salary = df.sort_values(by="Salary", ascending=False)
print("Employees Sorted by Salary")
print(sorted_salary)