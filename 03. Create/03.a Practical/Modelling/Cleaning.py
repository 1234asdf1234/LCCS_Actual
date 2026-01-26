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

outlier_index = 0
for i in df.index:
    risk = round(risk_def(df.loc[i, "ISI"], df.loc[i, "area"]), 1)
    df.loc[i, "risk"] = risk
    # clean the one outlier
    # this was identified in graphs
    if risk > 50:
        outlier_index = i
df = df.drop(outlier_index)


# output cleaned file
df.to_csv("forestfires_cleaned.csv", index=False)