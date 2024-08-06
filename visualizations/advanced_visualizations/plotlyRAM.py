import json
from plotly.subplots import make_subplots # type: ignore
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
    freeRam = [int(entry['memory']['available']) for entry in data]

    # Make a matrix of 4 subplots
    fig = make_subplots(rows=2, cols=1)
    
    # Subplot 1 (Used RAM):
    fig.add_scatter(x=timestamps, y=usedRam, mode="lines", line=dict(color="yellow"), marker=dict(size=5), name="Used RAM", row=1, col=1)
    fig.update_yaxes(title_text="Used RAM (MB)", row=1, col=1)

    # Subplot 2 (Free RAM):
    fig.add_scatter(x=timestamps, y=freeRam, mode="lines", line=dict(color="Green"), marker=dict(size=5), name="Free RAM", row=2, col=1)
    fig.update_yaxes(title_text="Free RAM (MB)", row=2, col=1)
    
    # Add limit / Total RAM
    fig.add_scatter(x=timestamps, y=totalRam, mode="lines", line=dict(color="Red", dash="dash"), name="CPU Capacity", row=[1,2], col=[1,1], showlegend=False)


    fig.update_layout(
        title_text="RAM Usage Over Time",
        title_font_size=30,
        title_x=0.5,
        title_xanchor="center",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_dark",
        hovermode="x unified"
    )
    for i in range(2):
        fig.update_xaxes(title_text="Time", row=i+1, col=1)

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

    time = datetime.strptime("2024-07-30 19:37:20", "%Y-%m-%d %H:%M:%S")
    # Select time for date and time for cpu and memory usage plots
    t1 = "2024-07-30 19:37:20"
    t2 = (time + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S")


    # specific test case
    # t1 = "2024-07-26 16:07:27"
    # t2 = "2024-07-26 16:38:00"

    FILEPATH = "../../json_datalog/memory_usage.json"
    
    plotData(grabData(t1, t2))
