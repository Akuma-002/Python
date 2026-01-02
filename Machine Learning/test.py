import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
df = pd.read_csv(r"data\Salary_Data.csv")

x1 = df[["YearsExperience"]]
x2 = df[["Age"]]
y = df["Salary"]

sns.pairplot(data=df)
plt.show()