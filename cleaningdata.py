import pandas as pd
import numpy as np

df = pd.read_csv("messydatafile.csv")
# print(df.head())

# print("Mistakes in file:")
# print(df.isnull().sum())

print(df['Rating'].dtype)
print(df['Founded'].dtype)
print(df['Revenue'].dtype)

df["Rating"].fillna(df["Rating"].median())
df["Founded"].fillna(df["Founded"].mean())
# df["Revenue"].fillna(df["Revenue"].mean(), inplace= True)

# df.replace([np.inf, -np.inf], np.nan, inplace=True)
# df.fillna(df.mean(), inplace=True)

df.to_csv("clean data file.csv")


