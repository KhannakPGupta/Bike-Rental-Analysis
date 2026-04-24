#Cell to represent hourly patterns
hourly_avg = df.groupby(df.index.hour)['cnt'].mean()
plt.figure(figsize=(10,5))
plt.plot(hourly_avg, marker='o')
plt.title("Average Bike Rentals by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()