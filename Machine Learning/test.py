import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({"name": ["cow", "dog", "cat", "horse"] })
le = LabelEncoder()
df["en_name"] = le.fit_transform(df["name"])
#print(df)
df2 = pd.read_csv("data\insurance_data_2000.csv")

df2["en_region"] = le.fit_transform(df2["region"])
print(df2["en_region"].unique())