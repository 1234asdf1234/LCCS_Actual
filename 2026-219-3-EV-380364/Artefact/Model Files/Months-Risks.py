# Analysing rules:
'''
1. check correlation between numerical factors
2. check risk distribution sorted by months
'''

import pandas as pd
import plotly.express as px

# list of months
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


df = pd.read_csv("forestfires_cleaned.csv")

# to perform .corr(), all strings should be removed
dfc = df.copy()
dfc.drop("month", axis=1, inplace=True)
corr = dfc.corr()
print(corr)

# distribution between months and risk
risk_by_month = df.groupby("month")["risk"].mean().reset_index()

# to improve sorting, give every month a numerical value
for i in risk_by_month.index:
    risk_by_month.loc[i, "month_value"] = months.index(risk_by_month.loc[i, "month"]) + 1

risk_by_month.sort_values("month_value", inplace=True)
print(risk_by_month)

fig = px.bar(
    risk_by_month, 
    x='month',
    y='risk',  
    title="Distribution of risk in months",
    labels={'risk': 'Fire Risk'},
    template="plotly_dark",
    color='month'  
)
fig.show()

