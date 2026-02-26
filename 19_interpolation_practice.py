import pandas as pd

data = {
  'Name': ['Ram', 'Shyam', 'Ghanshtam', 'Dhanshyam', 'Aditi', 'Harsh', 'Aditya', 'Resham'],
  'Age': [32, None, 29, None, 34, None, 23, 36]
}


df = pd.DataFrame(data)
print("Original Data:\n", df)

df['Age'] = df['Age'].interpolate()

print("\nAfter Interpolation:\n", df)