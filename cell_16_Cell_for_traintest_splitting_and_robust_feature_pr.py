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