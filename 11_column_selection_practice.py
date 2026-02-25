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

# -------------------- DISPLAY DATA --------------------

print("Data Frame:\n")
print(dt_frm)

# -------------------- COLUMN SELECTION --------------------

# Single column (returns a Series)
print("\nSingle column (returns a Series):\n")
print(dt_frm["Name"])

# Multiple columns (returns a DataFrame)
print("\nMultiple columns (returns a DataFrame):\n")
print(dt_frm[["Name", "Performance Score"]])