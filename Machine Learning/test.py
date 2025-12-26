import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("data\insurance_data_2000.csv")
print(dataset["charges"])

input_data = dataset.iloc[:,:-1]

output_data = dataset["charges"]

x_train, x_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.25)

print(x_test)