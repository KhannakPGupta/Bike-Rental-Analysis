#Cell to create baseline
baseline_pred = y_test.shift(1).fillna(method='bfill')
baseline_mae = mean_absolute_error(y_test, baseline_pred)
baseline_rmse = np.sqrt(mean_squared_error(y_test, baseline_pred))
print("Baseline MAE:", baseline_mae)
print("Baseline RMSE:", baseline_rmse)