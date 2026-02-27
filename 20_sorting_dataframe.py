import pandas as pd 

# -------------------- CREATE DATA -------------------- #

data = {
    'Name': ['Harsh', 'Palash', 'Akshit', 'Sanskar', 'Ronak'],
    'Age': [23, 21, 25, 28, 31],
    'Salary': [19000, 23000, 32000, 27000, 14000]
}

dt_frm = pd.DataFrame(data)

print("Original DataFrame:\n")
print(dt_frm)


# -------------------- SORT BY AGE ASCENDING -------------------- #

dt_frm.sort_values(by="Age", ascending=True, inplace=True)
print("\nSorted by Age (Ascending):\n")
print(dt_frm)


# -------------------- SORT BY AGE DESCENDING -------------------- #

dt_frm.sort_values(by="Age", ascending=False, inplace=True)
print("\nSorted by Age (Descending):\n")
print(dt_frm)


# -------------------- SORT BY MULTIPLE COLUMNS -------------------- #

dt_frm.sort_values(by=['Name', 'Age'], ascending=[True, False], inplace=True)
print("\nSorted by Name (A-Z) and Age (High-Low):\n")
print(dt_frm)