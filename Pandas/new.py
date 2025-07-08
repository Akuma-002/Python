import pandas as pd
import numpy as np
ar = pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({"name":["sahil", "Ram", "ema"], "marks":[100, 30, 45], "age":[20, 30, 1]})
dataF = pd.read_excel("data\employee_data.xlsx")
#print(dataF.head())
#print(dataF.describe())
#print(dataF.info())
#print(dataF["EmployeeID"])
#print(dataF.iloc[0])
print(df)
print(df.rename(columns={"name": "name1"}))
print(df)