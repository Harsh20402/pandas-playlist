import pandas as pd  # Import pandas library

# -------------------- READ CSV FILE --------------------

# Use forward slash (/) OR raw string (r"") to avoid path errors
csv_df = pd.read_csv("Files/sales_data_sample.csv", encoding="latin1")
# Alternative:
# csv_df = pd.read_csv(r"Files\sales_data_sample.csv", encoding="latin1")

# -------------------- DATA PREVIEW --------------------

# First 5 rows (default)
print("First 5 rows:\n")
print(csv_df.head())

# Last 5 rows (default)
print("\nLast 5 rows:\n")
print(csv_df.tail())

# First 10 rows
print("\nFirst 10 rows:\n")
print(csv_df.head(10))

# Last 15 rows
print("\nLast 15 rows:\n")
print(csv_df.tail(15))