import pandas as pd  # Import pandas library

# -------------------- JSON FILE READING --------------------

# Read JSON file from the "Files" folder
# Use forward slash (/) OR raw string (r"") to avoid path errors

json_df = pd.read_json("Files/sample_Data.json")
# Alternative:
# json_df = pd.read_json(r"Files\sample_Data.json")

# Display the DataFrame
print("Data from JSON file:\n")
print(json_df)