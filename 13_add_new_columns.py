import pandas as pd  # Import pandas library

# -------------------- CREATE SAMPLE DATA --------------------

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Harsh", "Soumya"],
    "Age": [32, 34, 29, 30, 34, 21, 23, 36],
    "Salary": [40000, 26000, 29000, 45000, 20000, 22000, 27000, 34000],
    "Performance Score": [65, 34, 76, 89, 91, 67, 56, 82]
}

# Convert dictionary to DataFrame
dt_frm = pd.DataFrame(data)

# -------------------- DISPLAY ORIGINAL DATA --------------------

print("Original Data Frame:\n")
print(dt_frm)

# -------------------- ADD NEW COLUMN (BONUS) --------------------

# Create Bonus column (10% of Salary)
dt_frm["Bonus"] = dt_frm["Salary"] * 0.10

print("\nData Frame after adding Bonus column:\n")
print(dt_frm)

# -------------------- INSERT COLUMN AT SPECIFIC POSITION --------------------

# Insert Employee ID at position 0
dt_frm.insert(
    0,
    "Emp_ID",
    ["Emp_001", "Emp_002", "Emp_003", "Emp_004",
     "Emp_005", "Emp_006", "Emp_007", "Emp_008"]
)

print("\nData Frame after inserting Emp_ID column at position 0:\n")
print(dt_frm)