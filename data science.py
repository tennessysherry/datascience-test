import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('school.csv')
# print(data)
# print(data.shape) # checks how many rows and columns there are in the data
# print(data.head()) # prints the first 5 rows
# print(data.head(20)) # prints the first 20 rows
# print(data.tail()) # prints the last 5 rows
print(data.isnull().sum()) # finds the null values in the data
print(data['Gender']) # prints the values in the column gender
data['Gender'].fillna(2, inplace=True) # replace missing with 2
print(data.isnull().sum())
sprint_mean = data['Sprint'].mean()
data['Sprint'].fillna(sprint_mean, inplace =True)
print(data.isnull().sum())
height_mean = data['Height'].mean()
data['Height'].fillna(sprint_mean, inplace =True)
print(data.isnull().sum())
