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
plt.grid(True)
#plt.ylim(0, 400)
plt.xticks()
#plt.bar(x, y)
#plt.pie(y, labels=x, autopct="%1.1f%%")
#plt.hist(y, bins=5)
#plt.scatter(y, z, marker="o")
plt.subplot(1, 2, 1)
plt.bar(x, y, color='red')
plt.title("day plot")

plt.subplot(1, 2, 2)
plt.plot(y, z)
plt.title("Usage")

plt.suptitle("All charts")
plt.tight_layout()
plt.savefig("nn.png", dpi=300, bbox_inches="tight")
plt.show()

