import pandas as pd
df = pd.read_csv("data\outlier_test_data_2000.csv")
z_score = (df["Feature1"] - df["Feature1"].mean())/(df["Feature1"].std())
df["z_score"] = z_score
new_df = df[(df["z_score"] <3) & (df["z_score"]>(-3))]

