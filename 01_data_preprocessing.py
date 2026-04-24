#Cell used to install all the files
!pip install statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import autocorrelation_plot

#Cell to fetch the file so that it gets redownloaded on it
!wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip
!unzip -q Bike-Sharing-Dataset.zip
import pandas as pd
df = pd.read_csv('hour.csv')
df.head()

import pandas as pd

#Cell to preprocess all the data
df = pd.read_csv('hour.csv')

df['datetime'] = pd.to_datetime(df['dteday']) + pd.to_timedelta(df['hr'], unit='h')
df.set_index('datetime', inplace=True)
df.sort_index(inplace=True)

df = df.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)