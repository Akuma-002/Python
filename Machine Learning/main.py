import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data\salary_prediction_dataset_2000.csv")

df2 = df.dropna()
print(df.head())
print(df2.head())
print(df.shape)
print(df2.shape)
nullV = (df.isnull().sum().sum())
notnullV = (df.shape[0] * df.shape[1]) - (df.isnull().sum().sum())
print(df.shape[0] * df.shape[1])
print((df.isnull().sum().sum())/df.shape[0] * df.shape[1])
val = [nullV, notnullV]
name = ["null", "not Null"]
plt.pie(val,labels=name, autopct="%1.1f%%")
plt.show()