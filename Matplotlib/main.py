import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\profit_data.csv")
df2 = pd.read_csv("data\profit_data_2.csv")
#print(df)
a = df["Day"]
print(a)

x = a.to_list()
y = df["Profit"].to_list()
z = df2["Profit"].to_list()
#plt.plot(x, y, label= "Sale Graph")
#plt.plot(x, z)
plt.xlabel("Days")
plt.ylabel("Profit")
plt.title("Sales report")
plt.legend()
plt.grid()
plt.ylim(0, 400)
plt.xticks()
#plt.bar(x, y)
plt.pie(y, labels=x, autopct="%1.1f%%")
plt.show()