import pandas as pd
import numpy as np

df = pd.read_csv("messydatafile.csv")
# print(df.head())

# print("Mistakes in file:")
# print(df.isnull().sum())

df_cat = df.select_dtypes(np.object_)
print(df_cat.head)
# df_num = df.select_dtypes(np.number)
# df_float = df.select_dtypes(np.float64)

print("Object Columns: \n",df_cat)
# print("Numeric Columns: \n",df_num)
# print("Float Columns: \n",df_float)

print(df["Size"].dtype)
missing_tokens = ["-", "--", "NA", "N/A", "n/a", "None", "none", "", "nan", "NaN", -1, -99]
df["Headquarters"] = df["Headquarters"].replace(missing_tokens, np.nan)
#Option 1
# if "Rating" in df.columns:
#     df["Rating"] =  df["Rating"].fillna(df["Rating"].median())

# if "Founded" in df.columns:
#     df["Founded"] = df["Founded"].fillna(df["Founded"].round().mean())


#Option 2
# df["Revenue"].fillna(df["Revenue"].mean(), inplace= True)

# df.replace([np.inf, -np.inf], np.nan, inplace=True)
# df.fillna(df.mean(), inplace=True)

df.to_csv("clean data file.csv")


