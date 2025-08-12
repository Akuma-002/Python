import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
df = pd.read_csv("data\outlier_sample_1000000.csv")
#sns.boxplot(x = "Feature1", data=df)
z_score = (df["Feature1"] - df["Feature1"].mean())/(df["Feature1"].std())
df["z_score"] = z_score
print(df["z_score"].std())
new_df = df[(df["z_score"] <df["z_score"].std()) & (df["z_score"]>(-(df["z_score"].std())))]
sns.displot(x = "z_score", data=new_df)
plt.show()

