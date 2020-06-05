import pandas as pd
from numpy import isnan

df = pd.read_csv('data/vgsales.csv')
df = df[['Name', 'Year', 'Genre', 'Platform', 'Publisher', 'Global_Sales']]
df = df.dropna()

df.to_csv('data/vgsales_cleaned.csv', index=False)