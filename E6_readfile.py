import pandas as pd

df = pd.read_csv("MOSFET_ID_VDS.csv") 

print("Columns:", df.columns)
print("Shape:", df.shape)
print(df.describe())
