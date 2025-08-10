import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt
df = pd.read_csv("data\outlier_test_data_2000.csv")
print(df.describe())

sns.boxplot(df["Feature1"])
plt.show()