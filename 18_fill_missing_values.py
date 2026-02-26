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


# -------------------- FILL ALL NULL VALUES WITH ZERO -------------------- #

zero_dt_frm = dt_frm.copy()
zero_dt_frm.fillna(0, inplace=True)

print("\nFilled with Zero:\n")
print(zero_dt_frm)


# -------------------- FILL ALL NULL VALUES WITH MEAN -------------------- #

mean_dt_frm = dt_frm.copy()

# Fill categorical column
mean_dt_frm['Name'].fillna('Unknown', inplace=True)

# Fill numeric columns with mean
mean_dt_frm['Age'].fillna(mean_dt_frm['Age'].mean(), inplace=True)
mean_dt_frm['Salary'].fillna(mean_dt_frm['Salary'].mean(), inplace=True)
mean_dt_frm['Performance Score'].fillna(mean_dt_frm['Performance Score'].mean(), inplace=True)

print("\nFilled Missing Values:\n")
print(mean_dt_frm)