# 🚲 Bike Rental Analysis & Demand Forecasting

This repository contains a rigorous, end-to-end time-series analysis and machine learning pipeline for forecasting bike rental demand. The project leverages the **UCI Bike Sharing Dataset**, applying advanced analytical techniques, exhaustive exploratory data analysis (EDA), and rolling feature engineering to build robust predictive models.

## 🧠 Project Approach & Methodology

The approach in this project heavily emphasizes an understanding of time-based phenomena, utilizing progressive steps to extract maximum value from temporal structures. 

The codebase was originally developed as a Jupyter Notebook but has been modularized into distinct analytical phases for better maintainability:

### 1. Data Preprocessing (`01_data_preprocessing.py`)
- **Dataset Acquisition**: Automated fetching of the dataset directly from the UCI ML Repository.
- **Temporal Indexing**: Fused the `dteday` (date) and `hr` (hour) columns into comprehensive `datetime` objects and configured them as the reliable index for the Pandas DataFrame.
- **Data Pruning**: Prevented target leakage by removing the linearly dependent `casual` and `registered` user counts, ensuring the model only trains on generalized independent variables. 

### 2. Time Series EDA (`02_time_series_eda.py`)
- **Multi-Granular Trend Analysis**: Evaluated human behavioral patterns across multiple levels by aggregating data mapping to hourly, daily, and monthly utilization frequencies.
- **Smoothed Trend & Seasonality**: Leveraged 7-day rolling calculations to dampen the noise overhead in high-frequency hourly data. Mapped and compared seasonal utilization behaviors.
- **Autocorrelation & Decomposition**: Utilized `statsmodels` to decompose the time-series continuously into *Trend*, *Seasonality*, and *Residuals*. Mapped autocorrelations to scientifically validate historical feature lag injection.
- **Anomaly Detection**: Pinpointed behavioral outliers mathematically using a rolling Z-score algorithm (thresh=3 standard deviations) isolated mapped anomalies against standard trajectories.

### 3. Feature Engineering (`03_feature_engineering.py`)
- **Lag Variables**: Since past rentals heavily influence future rentals, the pipeline engineers `lag_1`, `lag_24` (daily pattern), and `lag_168` (weekly pattern).
- **Cyclical Encoding**: To ensure the machine learning model understands the continuous, circular nature of time (for instance, that hour 23 transitions smoothly into hour 0), cyclical hours were encoded dynamically using `sine` and `cosine` transformations.
- **Sequential Splitting**: Respecting the principles of time-series analysis, the system avoids random data splitting. Instead, an 80/20 chronological train-test split secures model integrity against future-leakage.

### 4. Machine Learning Model (`04_model.py`)
- **Baseline Benchmarking**: Before deploying complex models, a naïve baseline (using simple historical carry-forward logic) was established. This guarantees that more sophisticated models are objectively improving on raw predictability.
- **Random Forest Regressor**: Selected an ensemble `RandomForestRegressor` as the primary predictive engine. Its non-linear structure elegantly tracks the deep interactions between diverse temporal, atmospheric, and lagged features.
- **Evaluation Mechanics**: Models are assessed comprehensively primarily utilizing MAE (Mean Absolute Error) & RMSE (Root Mean Squared Error).
- **Data Visualization Validation**: Deploys overlapping predictive vs. actual plots across both continuous test sets and zoomed-in 200-hour granular scopes to visually validate tracking accuracy across high-variance spikes.

## 🗂 File Structure
* **`01_data_preprocessing.py`**: Indexing, downloading, and data framing.
* **`02_time_series_eda.py`**: Visualizations, decompositions, and anomalies.
* **`03_feature_engineering.py`**: Lag engineering, sine-cosine transforms, timeline splitting.
* **`04_model.py`**: Model training, predictions, errors output, and final plots.
* **`SRM_Insider_Bike_Rental_Analysis.ipynb`**: The original complete Jupyter Notebook.

## 🚀 How to Run Locally

1. Create a virtual environment and ensure dependencies are installed:
   ```bash
   pip install pandas numpy matplotlib scikit-learn statsmodels
   ```
2. Execute the modules sequentially to replicate the analytical pipeline.
   ```bash
   python 01_data_preprocessing.py
   python 02_time_series_eda.py
   python 03_feature_engineering.py
   python 04_model.py
   ```
*(Note: Because of the sequential dataframe mutations, running the `.py` files independently without persistent global states might require merging modules. For the quickest validation, run the unified Jupyter notebook.)*