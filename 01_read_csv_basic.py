import pandas as pd  # Import pandas library for data analysis

# -------------------- CSV FILE READING --------------------

# Read CSV file from the "Files" folder
# If the default encoding fails, try specifying encoding

# csv_df = pd.read_csv("Files/sales_data_sample.csv")  # Default encoding
# csv_df = pd.read_csv("Files/sales_data_sample.csv", encoding="utf-8")  # UTF-8 encoding

csv_df = pd.read_csv("Files/sales_data_sample.csv", encoding="latin1")  
# Using latin1 encoding (useful when UTF-8 gives decoding error)

# Display the DataFrame
print("Data from CSV file:\n")
print(csv_df)