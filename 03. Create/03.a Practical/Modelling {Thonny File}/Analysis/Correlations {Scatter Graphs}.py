import plotly.graph_objects as go
import pandas as pd

def smokingMortality():
    df = pd.read_csv('data.csv')
    
    fig = go.Figure() # Creates an 'empty’ canvas for graph
    fig.add_trace(go.Scatter( 
        x=df['heart_rate'], # x-axis column data
        y=df['total_score'],  # y=axis column data
        mode='markers', # lines on graph and points on lines
        #name='Heart Rate'
    ))
    # Labels and Theme
    fig.update_layout(
        title="Scatter Plot:  Correlation of Heart Data and Health",
        xaxis_title="Heart Rate",
        yaxis_title="Health Level:  0 = Very Poor  5 = Excellent",
        template="plotly_dark" # plotly_white
    )
    fig.show() # Show Chart
smokingMortality()
