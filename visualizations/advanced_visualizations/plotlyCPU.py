import json
from datetime import datetime, timedelta
from plotly.subplots import make_subplots # type: ignore

FILEPATH = "../json_datalog/cpu_usage.json"

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


# Function to plot data
def plotData(data):

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    # Set the Plotting parameters
    totalCpu = [100 for datalog in data]
    totalUsepct = [sum([ float(datalog['cpu'][log]) for log in datalog['cpu'] if log != 'idle']) for datalog in data]
    systemPct = [float(datalog['cpu']['system']) for datalog in data]
    userPct = [float(datalog['cpu']['user']) for datalog in data]
    nicePct = [float(datalog['cpu']['nice']) for datalog in data]
    idlePct = [float(datalog['cpu']['idle']) for datalog in data]
    waitPct = [float(datalog['cpu']['wait']) for datalog in data]
    hiPct = [float(datalog['cpu']['hi']) for datalog in data]
    siPct = [float(datalog['cpu']['si']) for datalog in data]
    stPct = [float(datalog['cpu']['st']) for datalog in data]

    # Make a matrix of 4 subplots
    fig = make_subplots(rows=2, cols=2)

    
    # Subplot 1 (Total percentage):
    fig.add_scatter(x=timestamps, y=totalUsepct, mode="lines", line=dict(color="Blue"), marker=dict(size=5), name="Total pct of CPU in use", row=1, col=1)
    
    # Subplot 2 (Idle percentage):
    fig.add_scatter(x=timestamps, y=idlePct, mode="lines", line=dict(color="White"), marker=dict(size=5), name="Total pct of CPU idle", row=1, col=2)

    # Subplot 3 (Total Percentage semi-breakdown):

    # Make the trace for systemPct
    fig.add_scatter(x=timestamps, y=systemPct, mode="lines", line=dict(color="Grey"), marker=dict(size=5), name="System Processes", row=2, col=1)
    # Make the trace for userPct
    fig.add_scatter(x=timestamps, y=userPct, mode="lines", line=dict(color="Green"), marker=dict(size=5), name="User Processes", row=2, col=1)
    # Make the trace for nicePct
    fig.add_scatter(x=timestamps, y=nicePct, mode="lines", line=dict(color="Pink"), marker=dict(size=5), name="Nice Processes", row=2, col=1)


    # Subplot 4 (Background Processes)
    # Make the trace for waitPct
    fig.add_scatter(x=timestamps, y=waitPct, mode="lines",line=dict(color="Orange"), marker=dict(size=5), name="Wait Processes", row=2, col=2)
    # Make the trace for hiPct
    fig.add_scatter(x=timestamps, y=hiPct, mode="lines", line=dict(color="Purple"), marker=dict(size=5), name="Hardware Interrupts", row=2, col=2)
    # Make the trace for siPct
    fig.add_scatter(x=timestamps, y=siPct, mode="lines", line=dict(color="Brown"), marker=dict(size=5), name="Software Interrupts", row=2, col=2)
    # Make the trace for stPct
    fig.add_scatter(x=timestamps, y=stPct, mode="lines", line=dict(color="Yellow"), marker=dict(size=5), name="Steal Time", row=2, col=2)
    
    # Make the a limit-trace for all subplots
    fig.add_scatter(x=timestamps, y=totalCpu, mode="lines", line=dict(color="Red", dash="dash"), name="CPU Capacity", row=[1,1,2,2], col=[1,2,1,2], showlegend=False)

    # Update axis-labels for all subplots
    for row in range(1, 3):
        for col in range(1, 3):
            fig.update_yaxes(title_text="CPU Usage (%)", row=row, col=col)
            fig.update_xaxes(title_text="Time", row=row, col=col)
    

    # fig.update_traces()
    fig.update_layout(
        title_text="System Monitoring Dashboard - CPU",     # Update Title
        title_font_size=30,     # Set font size
        title_x=0.5,
        title_xanchor="center",
        title_y=0.95,
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
    
    fig.update_xaxes(tickformat="%H:%M:%S")     # Format time

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

    FILEPATH = "../../json_datalog/cpu_usage.json"

    plotData(grabData(t1, t2))



