import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({"name": ["cow", "dog", "cat", "horse"] })
le = LabelEncoder()
df["en_name"] = le.fit_transform(df["name"])
print(df)