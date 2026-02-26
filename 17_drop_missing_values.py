import pandas as pd  # Import pandas library


# -------------------- CREATE SAMPLE DATA -------------------- #

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", None, "Harsh", "Soumya"],
    "Age": [32, None, 29, 30, None, 21, 23, 36],
    "Salary": [40000, 26000, 29000, None, 20000, 22000, 27000, None],
    "Performance Score": [65, None, 76, None, 91, 67, 56, 82]
}

dt_frm = pd.DataFrame(data)


# -------------------- DISPLAY ORIGINAL DATA -------------------- #

print("Original DataFrame:\n")
print(dt_frm)


# -------------------- DROP ROWS WITH MISSING VALUES (axis=0) -------------------- #

# axis=0 → Drops rows that contain any missing value
dt_frm_rows = dt_frm.copy()  # Create copy to preserve original
dt_frm_rows.dropna(axis=0, inplace=True)

print("\nAfter Dropping Rows (axis=0):\n")
print(dt_frm_rows)


# -------------------- DROP COLUMNS WITH MISSING VALUES (axis=1) -------------------- #

# axis=1 → Drops columns that contain any missing value
dt_frm_columns = dt_frm.copy()  # Create another copy
dt_frm_columns.dropna(axis=1, inplace=True)

print("\nAfter Dropping Columns (axis=1):\n")
print(dt_frm_columns)