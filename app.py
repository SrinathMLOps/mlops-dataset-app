import pandas as pd

df = pd.read_csv("data/sample.csv")
print("Rows:", len(df))
print("Summary:")
print(df.describe(include='all'))
