import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/netflix_movies_sample_1000.csv")

print(df.info())

df = df.dropna(subset=['movie_id', 'title', 'release_year'])