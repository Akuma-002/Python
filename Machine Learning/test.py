import pandas as pd
df = pd.DataFrame({"name":["Ram", "Sam", "sahil", "Sam"], "age": [12, 14, 18, 14]})
df = df.drop_duplicates()
print(df)