# cleaning rules

'''
1. X,Y are unnecessary as they are indentifiers for each area
2. The risk indicator is marked by the following rules:
risk = ISI + area / 5
3. drop rain, day as not considered in model
'''

import pandas as pd

df = pd.read_csv("forestfires.csv")

# drop columns
df.drop("X", axis=1, inplace=True)
df.drop("Y", axis=1, inplace=True)
df.drop("rain", axis=1, inplace=True)
df.drop("day", axis=1, inplace=True)

# add risk column
def risk_def(isi, area):
    if area > 0:
        return isi * 1.2
    return isi

for i in df.index:
    df.loc[i, "risk"] = round(risk_def(df.loc[i, "ISI"], df.loc[i, "area"]), 1)

# output cleaned file
df.to_csv("forestfires_cleaned.csv", index=False)