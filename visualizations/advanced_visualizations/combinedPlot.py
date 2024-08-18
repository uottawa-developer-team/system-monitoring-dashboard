import json 
from datetime import datetime, timedelta
from plotly.subplots import make_subplots # type: ignore
import os
CPU_FILEPATH = os.path.join(os.path.dirname(__file__), "../json_datalog/cpu_usage.json")
MEM_FILEPATH = os.path.join(os.path.dirname(__file__), "../json_datalog/memory_usage.json")
DISK_FILEPATH = os.path.join(os.path.dirname(__file__), "../json_datalog/disk_data.json")
NET_FILEPATH = os.path.join(os.path.dirname(__file__), "../json_datalog/network_data.json")

# Function to grab data
def grabData(startDate, endDate, FILEPATH):

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



def plotCpu(t1, t2, file, figure, row=1, col=1):

    # Grab Data
    data = grabData(t1, t2, file)

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    # Set the Plotting parameters
    totalCpu = [100 for datalog in data]
    totalUsepct = [sum([ float(datalog['cpu'][log]) for log in datalog['cpu'] if log != 'idle']) for datalog in data]

     # Subplot 1 (Total percentage):
    figure.add_scatter(x=timestamps, y=totalUsepct, mode="lines", line=dict(color="Blue"), marker=dict(size=5), name="Total pct of CPU in use", row=row, col=col)
     # Make the a limit-trace for all subplots
    figure.add_scatter(x=timestamps, y=totalCpu, mode="lines", line=dict(color="Red", dash="dash"), name="CPU Capacity", row=row, col=col, showlegend=True)


    figure.update_yaxes(title_text="CPU Usage (%)", row=row, col=col)
    figure.update_xaxes(
        title_text="Time",
        range=[min(timestamps), max(timestamps)],
        fixedrange=True,
        matches='x',
        type='date',
        row=row, 
        col=col
    )


def plotMem(t1, t2, file, figure, row=1, col=2):

    # Grab Data
    data = grabData(t1, t2, file)

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    totalRam = [int(entry['memory']['total']) for entry in data]
    usedRam = [int(entry['memory']['used']) for entry in data]

    # Make a trace for the Used RAM
    figure.add_scatter(
        x=timestamps,
        y=usedRam,
        mode="lines",
        line=dict(color="yellow"),
        marker=dict(size=5),
        name="Used RAM",
        row=row,
        col=col
    )
     
    # Make a trace for the total RAM
    figure.add_scatter(
        x=timestamps,
        y=totalRam,
        mode="lines",
        line=dict(color="red", dash="dash"),
        name="RAM Capacity",
        row=row,
        col=col,
        showlegend=True
    )

    figure.update_yaxes(title_text="RAM Usage (MB)", row=row, col=col)
    figure.update_xaxes(
        title_text="Time", 
        type="date",
        range=[min(timestamps), max(timestamps)],
        fixedrange=True,
        matches='x',
        row=row, 
        col=col
        )

def plotDisk(t1_disk, t2, file, figure, row=2, col=1):

    # Grab Data
    data = grabData(t1_disk, t2, file)

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

     # Find the name of disk(s)
    disks = [ data[-1]['disk'][i]['device'] for i in range (len(data[-1]['disk']))]

    # Make a list of the disk capacities 
    capacities = [float(data[-1]['disk'][disks.index(disk)]['avail'][:-1])
                  if (data[-1]['disk'][disks.index(disk)]['avail'][-1]) == "G"
                   else float(data[-1]['disk'][disks.index(disk)]['avail'][:-1])/1024 for disk in disks]

    # Find the index of max capacities
    ind_max = capacities.index(max(capacities))

        
    availSpace = float(data[-1]['disk'][ind_max]['avail'][:-1]) 
    usedSpace = float(data[-1]['disk'][ind_max]['used'][:-1]) if data[-1]['disk'][ind_max]['used'][-1] == "G" else float(data[-1]['disk'][ind_max]['used'][:-1])/1024 

    
    figure.add_pie(labels=['Used Space (GB)', 'Available Space (GB)'], 
        values=[usedSpace, availSpace],
        row=row, col=col,
        marker_colors=['#8b0a1a', '#32cd32'],  # Set the colors
        hoverinfo='label+value+percent',  # Display the percentage on hover
        textinfo='label+value+percent',  # Display the percentage on the chart
        textposition='inside',  # Position the text inside the pie
        showlegend=False,  # Hide the legend
        # pull=[0.1, 0.1],  # Explode the pie chart
        # insidetextorientation='radial',
        domain=dict(x=[0, 0.8], y=[0.1, 0.9]),
        hole=.1
        )
    
def plotNet(t1, t2, file, figure, row=2, col=2):

    # Grab Data
    data = grabData(t1, t2, file)

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    rx_bytes = [int(entry['network']['rx_bytes'])/(1024**3) for entry in data]
    tx_bytes = [int(entry['network']['tx_bytes'])/(1024**3) for entry in data]
    

    # Convert timestamps to datetime objects
    dt_timestamps = [datetime.strptime(t.strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S') for t in timestamps]

    # Calculate the time difference between consecutive timestamps
    time_diffs = [(dt_timestamps[i] - dt_timestamps[i-1]).total_seconds() / 60 for i in range(1, len(dt_timestamps))]

    # Calculate the average time difference
    avg_time_diff = sum(time_diffs) / len(time_diffs)

    # Set the bar width to half of the average time difference
    bar_width = avg_time_diff / 2

    figure.add_bar(x=timestamps, y=rx_bytes, name="Received Bytes", width=bar_width * 60 * 1000, row=row, col=col)  # Convert bar width to milliseconds
    figure.add_bar(x=timestamps, y=tx_bytes, name="Transmitted Bytes", width=bar_width * 60 * 1000,  row=row, col=col)  # Convert bar width to milliseconds

    # figure.add_bar(x=timestamps, y=rx_bytes, name="Received Bytes", row=row, col=col)
    # figure.add_bar(x=timestamps, y=tx_bytes, name="Transmitted Bytes", row=row, col=col)


    figure.update_yaxes(title_text="Network Usage (GB)", row=row, col=col)
    figure.update_xaxes(
        title_text="Time", 
        range=[min(timestamps), max(timestamps)],
        fixedrange=True,
        matches='x',
        row=row, 
        col=col)


    
def plot(t1, t2, t1_disk):

    # Create a figure with 2 rows and 2 columns
    fig = make_subplots(rows=2, cols=2, specs=[[{"type": "xy"}, {"type": "xy"}], [{"type": "pie"}, {"type": "xy"}]]) # subplot_titles=("CPU", "RAM", "DISK", "NET")
    
    plotCpu(t1, t2, CPU_FILEPATH, fig, row=1, col=1)
    plotMem(t1, t2, MEM_FILEPATH, fig, row=1, col=2)
    plotDisk(t1_disk, t2, DISK_FILEPATH, fig, row=2, col=1)
    plotNet(t1, t2, NET_FILEPATH, fig, row=2, col=2)


    # fig.update_traces()
    fig.update_layout(
        title_text="System Monitoring Dashboard - CPU, RAM, DISK, NETWORK",     # Update Title
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
        hovermode="x unified",
        plot_bgcolor='rgba(20, 20, 20, 0.5)',
        height=700,
        autosize=True  # Makes the plot responsive
    )
    fig.update_xaxes(
        tickformat="%H:%M:%S",
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1hr", step="hour", stepmode="backward"),
                dict(count=4, label="4hr", step="hour", stepmode="backward"),
                dict(count=8, label="8hr", step="hour", stepmode="backward"),
                dict(label="All", step="all")
            ]),
            bgcolor="rgba(255, 255, 255, 0.5)",  # Change the background color of the range selector
            font=dict(color="black"),   # Change the text color of the range selector buttons
        ),
        row=1,
        col=1
    )

    if __name__ == "__main__":
        
        config = {'displaylogo': False} # Config information

        fig.show(renderer="browser", config=config) # Overriding the default renderer

    else:
        return fig


    


if __name__ == "__main__":
    # runspace
    t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    t1_cmn = (t2 - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    t1_d = (t2 - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S")

    plot(t1_cmn,t2,t1_d)
