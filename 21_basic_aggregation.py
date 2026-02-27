import pandas as pd 

data = {
    'Name': ['Harsh', 'Palash', 'Akshit', 'Sanskar', 'Ronak'],
    'Age': [23, 21, 25, 28, 31],
    'Salary': [19000, 23000, 32000, 27000, 14000]
}

dt_frm = pd.DataFrame(data)

print("Original DataFrame:\n")
print(dt_frm)


# -------------------- BASIC AGGREGATION -------------------- #

print("\nAverage Age:", dt_frm["Age"].mean())
print("Total Salary:", dt_frm["Salary"].sum())
print("Maximum Salary:", dt_frm["Salary"].max())
print("Minimum Salary:", dt_frm["Salary"].min())
print("Count of Employees:", dt_frm["Name"].count())