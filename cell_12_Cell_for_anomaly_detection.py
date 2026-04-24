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