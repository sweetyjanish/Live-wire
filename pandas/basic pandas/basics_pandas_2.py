import pandas as pd  # Import the pandas library

# Read data from a CSV file and store it in a DataFrame called df
df = pd.read_csv('data.csv')

# Print the DataFrame
print(df) 

# Print the DataFrame as a complete string
print(df.to_string()) 

# Print the current maximum number of rows to display
print(pd.options.display.max_rows) 

# Maximize the number of rows to display
pd.options.display.max_rows = 9999

# Re-read the CSV file to apply the new display option
df = pd.read_csv('data.csv')

# Print the DataFrame again with the updated display settings
print(df) 

# Read data from a JSON file and store it in a DataFrame called df
df = pd.read_json('data.json')

# Print the DataFrame as a complete string
print(df.to_string()) 

# Create a DataFrame from a dictionary

