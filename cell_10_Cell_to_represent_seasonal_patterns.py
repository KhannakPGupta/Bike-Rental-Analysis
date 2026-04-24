#Cell to represent seasonal patterns
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
seasonal_avg = df.groupby('season')['cnt'].mean()
seasonal_avg.index = seasonal_avg.index.map(season_map)
seasonal_avg.plot(kind='bar', figsize=(8,5))
plt.title("Average Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Average Rentals")
plt.show()