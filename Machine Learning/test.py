import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv("data\outlier_sample_1000000.csv")
ss = MinMaxScaler ()
ss.fit(df[["Feature1"]])
df["Feature4"] = pd.DataFrame(ss.transform(df[["Feature1"]]), columns=["x"])
print(df)
sns.displot(df["Feature4"])
plt.show()