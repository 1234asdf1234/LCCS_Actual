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
for i in df.index:
    df.loc[i, "risk"] = round(df.loc[i, "ISI"] + df.loc[i, "area"] / 5, 1)

# output cleaned file
df.to_csv("forestfires_cleaned.csv", index=False)