from sklearn.datasets import load_iris
import pandas as pd
import csv

iris = load_iris()

myvar = pd.Series(iris)

print(myvar)
# name of csv file
filename = "university_records.csv"

X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
#g=iris.fields 
#h=iris.rows
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
 
    # writing the fields
    csvwriter.writerow(feature_names)
 
    # writing the data rows
    csvwriter.writerows(X)
   