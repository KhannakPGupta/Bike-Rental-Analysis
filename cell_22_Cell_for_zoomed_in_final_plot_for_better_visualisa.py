#Cell for zoomed in final plot for better visualisation
plt.figure(figsize=(15,6))
#Only first 200 points
plt.plot(y_test.index[:200], y_test.values[:200], label='Actual', linewidth=2)
plt.plot(y_test.index[:200], y_pred[:200], label='Predicted', linestyle='--')
plt.title("Zoomed View: Actual vs Predicted (First 200 Hours)", fontsize=14)
plt.xlabel("Time")
plt.ylabel("Number of Rentals")
plt.grid(alpha=0.3)
plt.legend()
plt.show()