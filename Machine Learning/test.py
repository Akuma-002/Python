import pandas as pd
import numpy as np
from sklearn.preprocessing import FunctionTransformer
df = pd.DataFrame({"name":["Ram", "Sam", "sahil", "Sam"], "age": [12, 14, 18, 14]})
ft = FunctionTransformer(func=np.log1p)
ft.fit(df["age"])
df["new"] = ft.transform(df["age"])
print(df)