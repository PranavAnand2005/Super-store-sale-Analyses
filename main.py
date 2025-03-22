import pandas as pd
import csv

df = pd.read_csv("SuperStore_Sales_Dataset.csv")
dn = pd.json_normalize(df)
display = pd.set_option("dsplay.max.columns",None)
print(dn)
print(display)