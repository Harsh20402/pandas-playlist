import pandas as pd  # Import pandas library

# -------------------- READ EXCEL FILE --------------------

# Use forward slash (/) or raw string to avoid path errors
excel_df = pd.read_excel("Files/sample_data.xlsx")
# Alternative:
# excel_df = pd.read_excel(r"Files\sample_data.xlsx")

# -------------------- DATA PREVIEW --------------------

# First 5 rows (default)
print("First 5 rows:\n")
print(excel_df.head())

# Last 5 rows (default)
print("\nLast 5 rows:\n")
print(excel_df.tail())

# First 10 rows
print("\nFirst 10 rows:\n")
print(excel_df.head(10))

# Last 15 rows
print("\nLast 15 rows:\n")
print(excel_df.tail(15))