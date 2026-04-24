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