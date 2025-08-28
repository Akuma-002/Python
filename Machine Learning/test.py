import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./data/employees.csv")
x = df[["designation", "address"]]
y = df["salary"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("X_train shape:", x_train.shape)
print("X_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print(df.shape)