import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\profit_data.csv")
#print(df)
a = df["Day"]
print(a)

x = a.to_list()
y = df["Profit"].to_list()

plt.plot(x, y)
plt.show()