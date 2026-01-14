import pandas as pd

df = pd.read_csv("forestfires_cleaned.csv")

# not numerical
df = df.drop("month", axis=1)

# not considered
df = df.drop("ISI", axis=1)
df = df.drop("area", axis=1)

print(df.corr())