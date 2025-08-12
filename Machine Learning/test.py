import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
df = pd.read_csv("data\outlier_test_data_2000.csv")
#sns.boxplot(x = "Feature1", data=df)
z_score = (df["Feature1"] - df["Feature1"].mean())/(df["Feature1"].std())
df["z_score"] = z_score
new_df = df[(df["z_score"] <3) & (df["z_score"]>(-3))]
sns.displot(x = "Feature1", data=df)
plt.show()
