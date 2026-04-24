#Cell to represent trends
plt.figure(figsize=(15,5))
plt.plot(df['cnt'], linewidth=0.5)
plt.title("Bike Rentals Over Time (Overall Trend)")
plt.xlabel("Time")
plt.ylabel("Number of Rentals")
plt.show()

#Cell to represent hourly patterns
hourly_avg = df.groupby(df.index.hour)['cnt'].mean()
plt.figure(figsize=(10,5))
plt.plot(hourly_avg, marker='o')
plt.title("Average Bike Rentals by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()

#Cell to represent daily patterns
daily_avg = df.groupby(df.index.dayofweek)['cnt'].mean()
plt.figure(figsize=(8,5))
plt.plot(daily_avg, marker='o')
plt.title("Average Rentals by Day of Week")
plt.xlabel("Day (0=Mon, 6=Sun)")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()

#Cell to represent monthly patterns
monthly_avg = df.groupby(df.index.month)['cnt'].mean()
plt.figure(figsize=(10,5))
plt.plot(monthly_avg, marker='o')
plt.title("Average Rentals by Month")
plt.xlabel("Month")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()

#Cell to represent smoothed seasonal trends since last one was too noisy
plt.figure(figsize=(15,5))
df['cnt'].rolling(window=168).mean().plot()
plt.title("Smoothed Trend (7-Day Rolling Average)")
plt.xlabel("Time")
plt.ylabel("Average Rentals")
plt.show()

#Cell to represent seasonal patterns
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
seasonal_avg = df.groupby('season')['cnt'].mean()
seasonal_avg.index = seasonal_avg.index.map(season_map)
seasonal_avg.plot(kind='bar', figsize=(8,5))
plt.title("Average Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Average Rentals")
plt.show()

#Cell for autocorrelation
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
autocorrelation_plot(df['cnt'])
plt.title("Autocorrelation of Bike Rentals")
plt.xlabel("Lag (hours)")
plt.ylabel("Autocorrelation")
plt.grid(alpha=0.3)
plt.show()

#Cell for anomaly detection
window = 24  # 24 hours (daily cycle)
df['rolling_mean'] = df['cnt'].rolling(window).mean()
df['rolling_std'] = df['cnt'].rolling(window).std()
df['z_score'] = (df['cnt'] - df['rolling_mean']) / df['rolling_std']
threshold = 3
anomalies = df[np.abs(df['z_score']) > threshold]
print("Number of anomalies:", len(anomalies))
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.scatter(anomalies.index, anomalies['cnt'])
plt.title("Detected Anomalies Only")
plt.show()

#Cell for decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
ts = df['cnt'].dropna()
decomp = seasonal_decompose(ts, model='additive', period=24)
fig = decomp.plot()
fig.set_size_inches(12, 8)
plt.show()