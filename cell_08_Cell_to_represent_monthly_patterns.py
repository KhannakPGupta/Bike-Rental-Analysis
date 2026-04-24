#Cell to represent monthly patterns
monthly_avg = df.groupby(df.index.month)['cnt'].mean()
plt.figure(figsize=(10,5))
plt.plot(monthly_avg, marker='o')
plt.title("Average Rentals by Month")
plt.xlabel("Month")
plt.ylabel("Average Rentals")
plt.grid(True)
plt.show()