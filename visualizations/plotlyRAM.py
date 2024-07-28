import json
import plotly.graph_objects as go
from datetime import datetime, timedelta

FILEPATH = "../json_datalog/memory_usage.json"

def grabData(startDate, endDate):
    with open(FILEPATH, 'r') as f:
        dataList = json.load(f) #load it as a list of dictionaries

    startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S') #define start and end dates of plotted data
    endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')

    croppedData = [entry for entry in dataList if startDate <= datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') <= endDate]

    return croppedData

def plotData(data):
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]
    totalRam = [int(entry['memory']['total']) for entry in data]
    usedRam = [int(entry['memory']['used']) for entry in data]

    fig = go.Figure(data=[
        go.Scatter(
            x=timestamps,
            y=totalRam,
            mode='lines',
            name='Total RAM',
            line=dict(color='red', dash='dash')
        ),
        go.Scatter(
            x=timestamps,
            y=usedRam,
            mode='lines',
            name='Used RAM',
            line=dict(color='yellow')
        )
    ])

    fig.update_layout(
        title_text="RAM Usage Over Time",
        title_font_size=30,
        title_x=0.5,
        title_xanchor="center",
        xaxis_title="Time",
        yaxis_title="RAM Usage (MB)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_dark"
    )

    fig.update_xaxes(tickformat="%H:%M:%S")

    if __name__ == "__main__":

        config = {'displaylogo': False} # Config information

        fig.show(renderer="browser", config=config) # Overriding the default renderer

        # from dash import Dash, dcc, html

        # app = Dash()
        # app.layout = html.Div([
        #     dcc.Graph(figure=fig)
        # ])

        # app.run_server(debug=True, use_reloader=False)

    else:
        return fig


if __name__ == "__main__":
    # runspace
    t1 = (datetime.now() - timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S")
    t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # specific test case
    # t1 = "2024-07-26 16:07:27"
    # t2 = "2024-07-26 16:38:00"

    plotData(grabData(t1, t2))
