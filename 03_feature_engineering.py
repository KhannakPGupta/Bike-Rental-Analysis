#Cell for feature engineering
df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek
df['month'] = df.index.month
df['is_weekend'] = df['dayofweek'].isin([5,6]).astype(int)
df['lag_1'] = df['cnt'].shift(1)
df['lag_24'] = df['cnt'].shift(24)
df['lag_168'] = df['cnt'].shift(168)
df['rolling_mean_24'] = df['cnt'].rolling(24).mean()
df['hour_sin'] = np.sin(2*np.pi*df['hour']/24)
df['hour_cos'] = np.cos(2*np.pi*df['hour']/24)
df.dropna(inplace=True)

# This cell's functionality for data cleaning and numeric column selection
# has been integrated into the 'train-test splitting' cell to consolidate steps.

#Cell for train-test splitting and robust feature preparation
import numpy as np
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
X = df.drop('cnt', axis=1)
y = df['cnt']
X = X.select_dtypes(include=[np.number])
split = int(len(df) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]