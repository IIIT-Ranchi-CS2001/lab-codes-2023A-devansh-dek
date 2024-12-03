import pandas as pd
import numpy as np

# Loading the DataSet
file_path = 'AQI_Data.csv'
df = pd.read_csv(file_path)

# 1. Display the first 5 rows of the dataset
print("First 5 rows of the dataset: \n")
print(df.head())

# 2. Display the last 6 rows of the dataset
print("Last 6 rows of the dataset: \n")
print(df.tail(6))

# 3. Show the summary statistics for all numeric columns
print("Summary statistics for numeric columns: \n")
print(df.describe())

# 4. Use NumPy to compute the mean AQI, PM2.5, and PM10 values for each city
# Group data by 'City' and compute means
mean_values = df.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean()
print("Mean AQI, PM2.5, and PM10 values for each city: \n")
print(mean_values)

# 5. Filter and display all rows where the PM2.5 level exceeds 100
# Count such rows for each city (without using value_counts)
filtered_rows = df[df['PM2.5'] > 100]
city_counts = {}
for city in filtered_rows['City']:
    city_counts[city] = city_counts.get(city, 0) + 1

print("Rows where PM2.5 level exceeds 100: \n")
print(filtered_rows)

print("Count of rows where PM2.5 > 100 for each city: \n")
print(city_counts)
