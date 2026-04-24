#Cell to fetch the file so that it gets redownloaded on it
!wget -q https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip
!unzip -q Bike-Sharing-Dataset.zip
import pandas as pd
df = pd.read_csv('hour.csv')
df.head()