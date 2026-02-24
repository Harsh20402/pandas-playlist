import pandas as pd  # Import pandas library

# -------------------- CREATE DATA --------------------

# Dictionary containing sample data
data = {
    "Name": ["Harsh", "Amit", "Sanskar", "Saket", "Ankit"],
    "Age": [23, 21, 28, 38, 26],
    "Location": ["Kolkata", "Nagpur", "Delhi", "Jammu", "Pune"]
}

# Convert dictionary to DataFrame
final_data = pd.DataFrame(data)

# Display DataFrame
print("Created DataFrame:\n")
print(final_data)

# -------------------- SAVE DATAFRAME --------------------

# Save as CSV
final_data.to_csv("Save_Data_Frames/output.csv", index=False)

# Save as Excel
final_data.to_excel("Save_Data_Frames/output.xlsx", index=False)

# Save as JSON
final_data.to_json("Save_Data_Frames/output.json", index=False)

print("\nFiles saved successfully.")