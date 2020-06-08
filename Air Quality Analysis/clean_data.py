import os
from datetime import datetime, date, time

import pandas as pd
import numpy as np

df = pd.DataFrame()

# combine the data from different stations
for entry in os.listdir('data/raw data'):
    filename = 'data/raw data/' + entry
    temp_df = pd.read_csv(filename, index_col=False)
    df = df.append(temp_df)

# get the number of null values in each column of DataFrame
print(df.isna().sum())

df = df.dropna()

date_df = pd.DataFrame()
dates = []
for index, data in df.iterrows():
    year = str(data['year'])

    if(data['month'] < 10):
        month = '0' + str(data['month'])
    else:
        month = str(data['month'])
    
    if(data['day'] < 10):
        day = '0' + str(data['day'])
    else:
        day = str(data['day'])

    if(data['hour'] < 10):
        hour = '0' + str(data['hour'])
    else:
        hour = str(data['hour'])
    
    date_string = year + month + day + hour + '0000'
    date = pd.to_datetime(date_string, format='%Y%m%d%H%M%S')
    dates = np.append(dates, date)

dates = np.array(dates)
df = df.drop(columns=['No','year','month','day', 'hour'])


# get the number of values after deleting the null values
df.loc[:,'datetime'] = pd.Series(dates, index=df.index)
df = df[['datetime', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'wd', 'WSPM', 'station']]
print(df.columns)
print(len(df))
df.to_csv('data/airquality_cleaned.csv', index=False)