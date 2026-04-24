#Cell to represent trends
plt.figure(figsize=(15,5))
plt.plot(df['cnt'], linewidth=0.5)
plt.title("Bike Rentals Over Time (Overall Trend)")
plt.xlabel("Time")
plt.ylabel("Number of Rentals")
plt.show()