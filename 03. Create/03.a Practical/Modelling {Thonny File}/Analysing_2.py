import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("forestfires_cleaned.csv")

# minimum value is 2.2
# thus start from 2


# grouping
div_start = 2

for i in df.index:
    temp = df.loc[i, "temp"]
    while temp >= div_start:
        div_start += 5
    df.loc[i, "temp_group"] = f"{div_start-5}-{div_start}"
    div_start = 2


risk_by_temp = df.groupby("temp_group")["risk"].mean().reset_index()

# sorting
for i in risk_by_temp.index:
    tg = risk_by_temp.loc[i, "temp_group"]
    risk_by_temp.loc[i, "t_index"] = tg[:tg.index("-")]

risk_by_temp["t_index"] = pd.to_numeric(risk_by_temp["t_index"], errors='coerce')

risk_by_temp.sort_values("t_index", inplace=True)

print(risk_by_temp)

'''
fig = px.bar(
    risk_by_temp, 
    x='temp_group',
    y='risk',  
    title="Distribution of risk in temperature groups",
    labels={'risk': 'Fire Risk'},
    template="plotly_white",
    color='temp_group'  
)

fig.show()
'''

fig = go.Figure()

fig.add_trace(go.Scatter( 
    x=risk_by_temp['temp_group'],  
    y=risk_by_temp['risk'],  
    mode='lines+markers',  
    name='Temp VS Risk'
))

fig.update_layout(
    title="Temperature and Fire Risk",
    xaxis_title="Temperature",
    yaxis_title="Risk",
    template="plotly_dark" 
)

fig.show()