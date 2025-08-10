import pandas as pd
df = pd.read_csv("data\sample_2000_rows.csv")
print(df)
print((df.isnull().sum()/len(df))*100)

df = df.dropna()
print((df.isnull().sum()/len(df))*100)
