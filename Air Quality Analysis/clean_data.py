import os

import pandas as pd

df = pd.DataFrame()

# combine the data from different stations
for entry in os.listdir('data/raw data'):
    filename = 'data/raw data/' + entry
    temp_df = pd.read_csv(filename, index_col=False)
    df = df.append(temp_df)

# get the number of null values in each column of DataFrame
print(df.isna().sum())

df = df.dropna()

# get the number of null values after deleting the null values
print(len(df))

df.to_csv('data/airquality_cleaned.csv', index=False)