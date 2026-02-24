import pandas as pd  # Import pandas library

# -------------------- EXCEL FILE READING --------------------
# pip install openpyxl

# Read Excel file from "Files" folder
# If you face path errors, use forward slash (/) or raw string (r"")

excel_df = pd.read_excel("Files/sample_data.xlsx")  
# Alternative:
# excel_df = pd.read_excel(r"Files\sample_data.xlsx")

# Display the DataFrame
print("Data from Excel file:\n")
print(excel_df)