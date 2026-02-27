import pandas as pd 

# -------------------- CREATE DATAFRAME -------------------- #

data = {
    'Name': ['Harsh', 'Palash', 'Akshit', 'Sanskar', 'Ronak'],
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance'],
    'Age': [23, 21, 25, 28, 31],
    'Salary': [19000, 23000, 32000, 27000, 14000]
}

dt_frm = pd.DataFrame(data)

print("Original DataFrame:\n")
print(dt_frm)


# -------------------- SINGLE COLUMN AGGREGATION -------------------- #

print("\nSalary Aggregation:")
print(dt_frm["Salary"].agg(["count", "sum", "mean", "min", "max"]))


# -------------------- MULTIPLE COLUMN AGGREGATION -------------------- #

print("\nAge & Salary Aggregation:")
print(dt_frm[['Age', 'Salary']].agg(['min', 'max', 'mean']))


# -------------------- GROUPBY AGGREGATION -------------------- #

grouped = dt_frm.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(grouped)