#Cell for training the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)