import pandas as pd

df = pd.read_csv('data.csv')

# Display the first 5 rows of the DataFrame
print(df.head())

# Display the last 5 rows of the DataFrame
print(df.tail())

# Display the DataFrame information
print(df.info())
