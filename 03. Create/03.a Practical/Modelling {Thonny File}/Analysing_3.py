import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("forestfires_cleaned.csv")

fig = go.Figure()

fig.add_trace(go.Scatter( 
    x=df['wind'], # x-axis column data
    y=df['risk'],  # y=axis column data
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

correlation = df["wind"].corr(df["risk"])
print(f"The correlation is {correlation}")
