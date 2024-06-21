import pandas as pd  # Import the pandas library

# Create a DataFrame from a dictionary
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar1 = pd.DataFrame(mydataset)
print(myvar1)

# Create a Series from a list
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Create a Series with custom indices
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

# Access a specific value in a Series using its index
print(myvar["y"])

# Create a Series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Create a Series with selected keys from a dictionary
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

# Locate rows in a DataFrame using integer-location based indexing
print(myvar1.loc[0])
print(myvar1.loc[[0, 1]])

# Create a DataFrame with named indexes
myvar1 = pd.DataFrame(mydataset, index=["day1", "day2", "day3"])
print(myvar1)

# Locate rows in a DataFrame using named indexes
print(myvar1.loc["day2"])
 