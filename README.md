# 🚲 Bike Rental Analysis & Demand Forecasting

This repository contains a rigorous, end-to-end time-series analysis and machine learning pipeline for forecasting bike rental demand. Leveraging the **UCI Bike Sharing Dataset**, this project applies advanced analytical techniques, exhaustive exploratory data analysis (EDA), and sophisticated rolling feature engineering to build highly responsive predictive models.

## 🧠 Core Patterns Discovered

During the extensive Exploratory Data Analysis, several distinct behavioral patterns were mapped that dictate urban bike-sharing demand:

### **High-Frequency Behavioral Rhythms**
- **Hourly Commuter Spikes (Bimodal Distribution):** Utilization distinctly surges during standard commuting hours (8:00 AM & 5:00 PM - 6:00 PM), strongly indicating that rentals are heavily driven by workforce transportation rather than purely recreational use.
- **Micro-Cyclical Patterns (Weekly):** A substantial drop-off occurs during weekends. However, weekend usage shifts from sharp commuter peaks to a flatter, wider plateau extending across mid-day hours, indicating a shift from utilitarian commuting to recreational cruising.
- **Seasonal & Macro-Trends:** Demand follows a clear parabolic curve over the months, peaking in warm summer/early-fall months (July–September) and severely plunging during harsh winter conditions, proving extreme temperature/weather elasticity.

---

## 🔬 Deep Methodological Approach

This analysis transcends basic regression by treating the dataset as a living, sequential time-series entity. The methodology is structured around four primary pillars:

### 1. Robust Data Preprocessing
- **Chronological Restructuring:** Fused the independent `dteday` (date) and `hr` (hour) attributes into unified continuous `datetime` objects. By converting this to the primary DataFrame index, the architecture natively supports Pandas' advanced temporal functions (like `.rolling()` and `.shift()`).
- **Elimination of Target Leakage:** Eradicated the sub-counts (`casual` and `registered`). Since predicting the sum total `cnt` is the primary objective, including its partial subsets would artificially inflate model confidence and invalidate the logic.

### 2. Time-Series Dynamics & Anomaly Tracking
- **Mathematical Smoothing:** Raw hourly data introduces chaotic high-frequency noise. A 168-hour (7-day) rolling average was injected to neutralize short-term variance and expose the true underlying macro-trends over the two years.
- **Additive Decomposition:** Deployed `statsmodels.tsa.seasonal_decompose` to break down the rentals stream into mathematically independent vectors:
  - **Trend**: The slow-moving macro trajectory of the platform's overall growth.
  - **Seasonal**: The mathematically repeating 24-hour micro-patterns.
  - **Residual**: The unexplained "chaos" left behind after stripping out predictable traits.
- **Rolling Z-Score Anomaly Detection:** Instead of flat thresholds, the system calculates algorithmic anomalies on the fly. By assessing the standard deviation of a tightly rolling 24-hour window, it isolates instances that break statistical normality by >3 Sigma (like sudden storms or major events) allowing clean analytical isolation of shocks.

### 3. Advanced Temporal Feature Engineering
Machine learning algorithms are mathematically "time-blind"; they do not innately understand that Hour 23 transforms directly into Hour 0. 
- **Trigonometric Time Encoding (Sine/Cosine Waves):** The pipeline forces the model to understand cyclical time continuity. Hours are transformed via radians into `sine` and `cosine` signals, feeding the algorithm an elegant, continuous mathematical loop representing the 24-hour cycle.
- **Autoregressive Lags:** Since weather and time alone don't explain immediate momentum (e.g., a burst of tourism continuing into the next hour), past truths are fed into the prediction of future truths. Engineered variables include `lag_1` (momentum), `lag_24` (daily mirror), and `lag_168` (weekly mirror).

### 4. Predictive Modeling & Objective Benchmarking
- **Establishing the Baseline Ceiling:** Developed a naïve "carry-forward" algorithm (predicting that the current hour's rentals will equal the prior hour's rentals exactly). This provides a strict, real-world floor to prove the complex model's worth against.
- **Random Forest Non-Linearity:** Given the complex, non-linear interactions of the variables (e.g., high humidity is fine if the temperature is low, but detrimental if the temperature is high), an ensemble `RandomForestRegressor` was deployed. The model elegantly isolates these thresholds without requiring explicitly bounded interaction terms.
- **Sequential Validation Engine:** Random splitting destroys temporal integrity. The model exclusively uses the oldest 80% of chronological data to train, and blind-predicts on the youngest 20%, ensuring the model is strictly evaluated on the "future."

## 🗂 Architecture mapping
* **`01_data_preprocessing.py`**: Indexing, downloading, and data framing.
* **`02_time_series_eda.py`**: Visualizations, decompositions, and anomalies.
* **`03_feature_engineering.py`**: Lag engineering, sine-cosine transforms, timeline splitting.
* **`04_model.py`**: Model training, predictions, errors output, and final plots.