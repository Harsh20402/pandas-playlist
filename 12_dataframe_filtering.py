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

# -------------------- FILTERING --------------------

# 1️⃣ Single condition
salary_filter = dt_frm[dt_frm["Salary"] > 30000]

print("\nEmployees with salary greater than 30000:\n")
print(salary_filter)

# 2️⃣ Multiple conditions using AND (&)
multi_filter_and = dt_frm[
    (dt_frm["Salary"] > 25000) &
    (dt_frm["Age"] >= 30) &
    (dt_frm["Age"] <= 35)
]

print("\nEmployees aged between 30-35 and salary > 25000:\n")
print(multi_filter_and)

# 3️⃣ Multiple conditions using OR (|)
multi_filter_or = dt_frm[
    (dt_frm["Age"] > 35) |
    (dt_frm["Performance Score"] > 90)
]

print("\nEmployees older than 35 OR performance score > 90:\n")
print(multi_filter_or)