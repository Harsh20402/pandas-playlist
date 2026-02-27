import pandas as pd

# -------------------- CREATE FIRST DATAFRAME -------------------- #

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Harsh', 'Amit', 'Ankit']
})

# -------------------- CREATE SECOND DATAFRAME -------------------- #

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['Rahul', 'Sohan', 'Riya']
})

# -------------------- ROW-WISE CONCATENATION (axis=0) -------------------- #

print("\nRow-wise Concatenation:")
row_concat = pd.concat([df1, df2], axis=0)
print(row_concat)


# -------------------- ROW-WISE CONCAT (Reset Index) -------------------- #

print("\nRow-wise Concatenation with Reset Index:")
row_concat_reset = pd.concat([df1, df2], axis=0, ignore_index=True)
print(row_concat_reset)


# -------------------- COLUMN-WISE CONCATENATION (axis=1) -------------------- #

df3 = pd.DataFrame({
    'Salary': [20000, 25000, 30000]
})

print("\nColumn-wise Concatenation:")
col_concat = pd.concat([df1, df3], axis=1, ignore_index = True)
print(col_concat)