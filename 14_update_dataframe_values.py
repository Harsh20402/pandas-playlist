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

# -------------------- UPDATE ENTIRE COLUMN --------------------

# Increase Salary by 5%
dt_frm["Salary"] = dt_frm["Salary"] * 1.05

print("\nAfter 5% Salary Increment:\n")
print(dt_frm)

# -------------------- UPDATE SPECIFIC CELL USING loc --------------------

# Change Age of first employee (index 0)
dt_frm.loc[0, "Age"] = 35

print("\nAfter Updating Age at index 0:\n")
print(dt_frm)