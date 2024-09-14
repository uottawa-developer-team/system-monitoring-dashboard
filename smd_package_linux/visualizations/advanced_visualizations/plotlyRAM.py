import json
from plotly.subplots import make_subplots # type: ignore
from datetime import datetime, timedelta
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "../../json_datalog/memory_usage.json")

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
    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.3)
    
    # Subplot 1 (Used RAM):
    fig.add_scatter(x=timestamps, y=usedRam, mode="lines", line=dict(color="yellow"), marker=dict(size=5), name="Used RAM", row=1, col=1)
    fig.update_yaxes(title_text="Used RAM (MB)", row=1, col=1)

    # Subplot 2 (Free RAM):
    fig.add_scatter(x=timestamps, y=freeRam, mode="lines", line=dict(color="Green"), marker=dict(size=5), name="Free RAM", row=2, col=1)
    fig.update_yaxes(title_text="Free RAM (MB)", row=2, col=1)
    
    # Add limit / Total RAM
    fig.add_scatter(x=timestamps, y=totalRam, mode="lines", line=dict(color="Red", dash="dash"), name="CPU Capacity", row=[1,2], col=[1,1], showlegend=False)


    fig.update_layout(
        title_text="System Monitoring Dashboard - RAM",
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
        hovermode="x unified",
        plot_bgcolor='rgba(20, 20, 20, 0.5)',
        height=700,
        autosize=True  # Makes the plot responsive
    )

    for i in range(2):
        fig.update_xaxes(
            title_text="Time",
            range=[min(timestamps), max(timestamps)],
            fixedrange=True,
            rangeslider=dict(
                visible=True,
                thickness=0.1
            ),
            matches='x',
            type='date',
            row=i+1, 
            col=1
        )

    # make range slector buttons    
    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=5, label="5m", step="minute", stepmode="backward"),
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=1, label="1hr", step="hour", stepmode="backward"),
                dict(label="All", step="all")
            ]),
            bgcolor="rgba(255, 255, 255, 0.5)",  # Change the background color of the range selector
            font=dict(color="black")  # Change the text color of the range selector buttons
        ),
        row=1,
        col=1
    )

    fig.update_xaxes(tickformat="%H:%M:%S")

    if __name__ == "__main__":

        config = {'displaylogo': False} # Config information

        fig.show(renderer="browser", config=config) # Overriding the default renderer

    else:
        return fig


if __name__ == "__main__":
    # runspace
    t2 = datetime.now()
    t1 = (t2 - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    
    plotData(grabData(t1, t2.strftime("%Y-%m-%d %H:%M:%S")))
