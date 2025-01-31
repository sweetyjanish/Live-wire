# cleaning using pandas

import pandas as pd  # Import the pandas library and alias it as pd

# Read the data.csv file and store it in a DataFrame called df
df = pd.read_csv('data.csv')

# Drop rows with missing values and create a new DataFrame
new_df = df.dropna() 
print(new_df.to_string())

# Drop rows with missing values in the original DataFrame
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())

# Replace all missing values with a specific value (130)
df = pd.read_csv('data.csv')
df.fillna(130, inplace=True)
print(df.to_string())

# Replace missing values in a particular column ('Calories') with a specific value (130)
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace=True)
print(df.to_string())

# Replace missing values in a particular column ('Calories') with the mean value of that column
df = pd.read_csv('data.csv')
mean_value = df["Calories"].mean()
df["Calories"].fillna(mean_value, inplace=True)
print(df.to_string())

# Replace missing values in a particular column ('Calories') with the median value of that column
df = pd.read_csv('data.csv')
median_value = df["Calories"].median()
df["Calories"].fillna(median_value, inplace=True)
print(df.to_string())

# Replace missing values in a particular column ('Calories') with the mode value of that column
df = pd.read_csv('data.csv')
mode_value = df["Calories"].mode()[0]
df["Calories"].fillna(mode_value, inplace=True)
print(df.to_string())





# cleaning wrong using pandas

import pandas as pd  # Import the pandas library and alias it as pd

# Read the data.csv file and store it in a DataFrame called df
df = pd.read_csv('data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# Remove rows where the 'Date' column has missing values
df.dropna(subset=['Date'], inplace=True)

# Locate and change the value in the 'Duration' column for the row with index 7
df.loc[7, 'Duration'] = 45

# Create a rule to change values in the 'Duration' column
# If 'Duration' is greater than 120, set it to 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Show duplicated rows
print(df.duplicated())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Calculate and show the correlation matrix
print(df.corr())




# ploting using pandas

import pandas as pd  # Import the pandas library
import matplotlib.pyplot as plt  # Import the matplotlib library for plotting

# Read the data.csv file and store it in a DataFrame called df
df = pd.read_csv('data.csv')

# Line plot of the DataFrame
df.plot()
plt.show()

# Scatter plot of 'Duration' vs 'Calories'
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

# Scatter plot of 'Duration' vs 'Maxpulse'
df.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

# Histogram of the 'Duration' column
df["Duration"].plot(kind='hist')
plt.show()


