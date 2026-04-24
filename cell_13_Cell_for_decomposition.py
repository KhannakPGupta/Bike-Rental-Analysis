#Cell for decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
ts = df['cnt'].dropna()
decomp = seasonal_decompose(ts, model='additive', period=24)
fig = decomp.plot()
fig.set_size_inches(12, 8)
plt.show()