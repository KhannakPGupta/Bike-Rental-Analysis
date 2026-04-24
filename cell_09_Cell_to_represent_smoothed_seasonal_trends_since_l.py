#Cell to represent smoothed seasonal trends since last one was too noisy
plt.figure(figsize=(15,5))
df['cnt'].rolling(window=168).mean().plot()
plt.title("Smoothed Trend (7-Day Rolling Average)")
plt.xlabel("Time")
plt.ylabel("Average Rentals")
plt.show()