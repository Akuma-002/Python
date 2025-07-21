import pandas as pd

df = pd.read_csv("data\salary_prediction_dataset_2000.csv")

df2 = df.dropna()
print(df.head())
print(df2.head())
print(df.shape)
print(df2.shape)
print((df.isnull().sum()/df.shape[0])*100)