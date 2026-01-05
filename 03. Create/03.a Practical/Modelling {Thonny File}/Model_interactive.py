import Model
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("forestfires_cleaned.csv")

high = 0
med = 0
low = 0

for i in df.index:
    df.loc[i, "score"] = Model.scoring(df.loc[i, "month"], df.loc[i, "temp"], df.loc[i, "wind"],
                  df.loc[i, "RH"], df.loc[i, "DMC"], df.loc[i, "DC"], df.loc[i, "FFMC"])
    s = df.loc[i, "score"]
    if s >= 16:
        high += 1
    elif s >= 13:
        med += 1
    else:
        low += 1

fig = go.Figure()

fig.add_trace(go.Scatter( 
    x=df.index, # x-axis column data
    y=df['score'],  # y=axis column data
    mode='markers', # lines on graph and points on lines
    #name='Heart Rate'
))
# Labels and Theme
fig.update_layout(
    title="Scatter Plot: Humidity against fire risk",
    xaxis_title="Humidity",
    yaxis_title="Risk",
    template="plotly_white" # plotly_white
)
fig.show() # Show Chart

print(f"{high}, {med}, {low}")