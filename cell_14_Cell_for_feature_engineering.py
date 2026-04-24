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