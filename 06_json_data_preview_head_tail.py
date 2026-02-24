import pandas as pd  # Import pandas library

# -------------------- READ JSON FILE --------------------

# Use forward slash (/) OR raw string (r"") to avoid path errors
json_df = pd.read_json("Files/sample_Data.json")
# Alternative:
# json_df = pd.read_json(r"Files\sample_Data.json")

# -------------------- DATA PREVIEW --------------------

# First 5 rows (default)
print("First 5 rows:\n")
print(json_df.head())

# Last 5 rows (default)
print("\nLast 5 rows:\n")
print(json_df.tail())

# First 10 rows
print("\nFirst 10 rows:\n")
print(json_df.head(10))

# Last 15 rows
print("\nLast 15 rows:\n")
print(json_df.tail(15))