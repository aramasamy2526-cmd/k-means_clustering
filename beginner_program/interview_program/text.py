import pandas as pd
import re

df = pd.read_csv(r"E:\Ram\python\test.csv")

# convert everything to string first
df["price"] = df["price"].astype(str)

# remove all characters except 0-9 and .
df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True)

# convert to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")

print(df)
