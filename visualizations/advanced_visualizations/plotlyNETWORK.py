import json
from datetime import datetime, timedelta
import plotly.graph_objects as go # type: ignore

FILEPATH = "../json_datalog/network_data.json"


def grabData(startDate, endDate):

    # Load the file as a list of dictionaries using the json module
    with open(FILEPATH, 'r') as f:
        dataList = json.load(f)

    # Format dates
    startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
    endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')

    # Extract Data within Date ranges
    croppedData = [datalog for datalog in dataList if startDate <= datetime.strptime(datalog['timestamp'], '%Y-%m-%d %H:%M:%S') <= endDate]
     
    # Return Extracted Data
    return croppedData


def plotData(data):
    
    timestamps = [entry['timestamp'] for entry in data]
    rx_bytes = [int(entry['network']['rx_bytes'])/(1024**2) for entry in data]
    tx_bytes = [int(entry['network']['tx_bytes'])/(1024**2) for entry in data]


    fig = go.Figure()
    fig.add_bar(x=timestamps, y=rx_bytes, name="Received Bytes")
    fig.add_bar(x=timestamps, y=tx_bytes, name="Transmitted Bytes")
    fig.update_layout(
        title_text="System Monitoring Dashboard - Network Usage",
        title_font_size=30,
        title_x=0.5,
        xaxis_title="Time",
        yaxis_title="MegaBytes (MB)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_dark",
        barmode='group',
        hovermode="x unified",
        plot_bgcolor='rgba(20, 20, 20, 0.5)',
        height=630,
        autosize=True  # Makes the plot responsive
    )

    fig.update_xaxes(
        tickformat="%H:%M:%S",
        range=[min(timestamps), max(timestamps)],
        fixedrange=True,
        rangeslider=dict(
            visible=True,
            thickness=0.1
        ),
        type='date',
        rangeselector=dict(
            buttons=list([
                dict(count=5, label="5m", step="minute", stepmode="backward"),
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(label="All", step="all")
            ]),
            bgcolor="rgba(255, 255, 255, 0.5)",  # Change the background color of the range selector
            font=dict(color="black"),   # Change the text color of the range selector buttons
        ),
    )

    if __name__ == "__main__":

        config = {'displaylogo': False} # Config information

        fig.show(renderer="browser", config=config) # Overriding the default renderer

    else:
        return fig



if __name__ == "__main__":
    # runspace
    t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    t1 = (t2 - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

    FILEPATH = "../../json_datalog/network_data.json"
    
    plotData(grabData(t1, t2))