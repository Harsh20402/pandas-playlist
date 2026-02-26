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

# -------------------- DROP SINGLE COLUMN --------------------

dt_frm.drop(columns=["Salary"], inplace=True)

print("\nAfter Dropping 'Salary' Column:\n")
print(dt_frm)

# -------------------- DROP MULTIPLE COLUMNS --------------------

dt_frm.drop(columns=["Performance Score", "Age"], inplace=True)

print("\nAfter Dropping 'Performance Score' and 'Age' Columns:\n")
print(dt_frm)