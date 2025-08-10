import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt
df = pd.read_csv("data\outlier_test_data_2000.csv")
q1 = df['Feature1'].quantile(0.25)
q3 = df['Feature1'].quantile(0.75)
IQR = q3 - q1
min_range = q1 - (1.5*IQR)
max_range = q3 + (1.5*IQR)
n_df = df[(df['Feature1']<=max_range) & (df['Feature1']>= min_range)]
print(df.shape)
print(n_df.shape)

sns.displot( x = "Feature1", data=df)
sns.displot( x = "Feature1", data=n_df)
plt.show()