import pandas as pd
import jovian as jv
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler as ss
plt.rcParams['font.size'] = 14
medDF = pd.read_csv("data\insurance_data_2000.csv")
numeric_ool = ['age', 'bmi', 'children']
scaler = ss()
scaler.fit(medDF[numeric_ool])

ss()

print(scaler.mean_)

print(scaler.var_)

scaled_inputs = scaler.transform(medDF[numeric_ool])
print(scaled_inputs)

cat_col = ['smoker', 'sex', 'region']
catagorical_data = medDF[cat_col].values
print(catagorical_data)