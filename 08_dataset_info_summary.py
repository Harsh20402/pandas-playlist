import pandas as pd  # Import pandas library

# -------------------- READ FILES --------------------

# CSV File
csv_df = pd.read_csv("Files/sales_data_sample.csv", encoding="latin1")

# Excel File
excel_df = pd.read_excel("Files/sample_data.xlsx")

# JSON File
json_df = pd.read_json("Files/sample_Data.json")

# -------------------- DISPLAY INFO --------------------

print("\n================ CSV FILE INFO ================\n")
print(csv_df.info())

print("\n================ EXCEL FILE INFO ================\n")
print(excel_df.info())

print("\n================ JSON FILE INFO ================\n")
print(json_df.info())