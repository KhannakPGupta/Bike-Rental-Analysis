import pandas as pd

#Cell to preprocess all the data
df = pd.read_csv('hour.csv')

df['datetime'] = pd.to_datetime(df['dteday']) + pd.to_timedelta(df['hr'], unit='h')
df.set_index('datetime', inplace=True)
df.sort_index(inplace=True)

df = df.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)