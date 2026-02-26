import pandas as pd  # Import pandas library for data manipulation


# -------------------- CREATE SAMPLE DATA -------------------- #

# Dictionary containing employee data
# Some values are intentionally kept as None to simulate missing data
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", None, "Harsh", "Soumya"],
    "Age": [32, None, 29, 30, None, 21, 23, 36],
    "Salary": [40000, 26000, 29000, None, 20000, 22000, 27000, None],
    "Performance Score": [65, None, 76, None, 91, 67, 56, 82]
}

# Convert dictionary into a Pandas DataFrame
dt_frm = pd.DataFrame(data)


# -------------------- DISPLAY ORIGINAL DATA -------------------- #

# Print the original DataFrame
print("Original Data Frame:\n")
print(dt_frm)


# -------------------- CHECK MISSING VALUES -------------------- #

# Display True/False matrix where:
# True  -> Missing value
# False -> Value exists
print("\nMissing Value Matrix (True = Missing):\n")
print(dt_frm.isnull())


# Count total missing values in each column
# True = 1 and False = 0, so sum() gives total missing count
print("\nMissing Values Count Per Column:\n")
print(dt_frm.isnull().sum())