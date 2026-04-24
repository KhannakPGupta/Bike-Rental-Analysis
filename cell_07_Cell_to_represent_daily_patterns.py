#Cell to represent daily patterns
daily_avg = df.groupby(df.index.dayofweek)['cnt'].mean()
plt.figure(figsize=(8,5))
plt.plot(daily_avg, marker='o')
plt.title("Average Rentals by Day of Week")
plt.xlabel("Day (0=Mon, 6=Sun)")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()