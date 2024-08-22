import json
from datetime import datetime, timedelta
from plotly.subplots import make_subplots # type: ignore
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "../json_datalog/disk_data.json")


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

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    # Find the name of disk(s)
    disks = [ data[-1]['disk'][i]['device'] for i in range (len(data[-1]['disk']))]

    # Sort the disk(s) name(s)
    disks = sorted(disks)

    # Use the length to determine the number of disks
    numOfDisks = len(disks)


    # Create subplots with a mix of 'xy' and 'pie' types
    fig = make_subplots(rows=numOfDisks, cols=2, specs=[[{"type": "xy"}, {"type": "pie"}] for _ in range(numOfDisks)],
                        subplot_titles=[disks[i//2][-4:] if i%2 != 0 else "" for i in range(numOfDisks*2)], vertical_spacing=0.3)


    for i in range(numOfDisks):

        # Extract the data for each disk
        capacity = [float(entry['disk'][i]['size'][:-1]) for entry in data]
        availSpace = [float(entry['disk'][i]['avail'][:-1]) for entry in data]
        usedSpace = [float(entry['disk'][i]['used'][:-1]) 
                     if entry['disk'][i]['used'][-1] == "G" else float(entry['disk'][i]['used'][:-1])/1024 
                     for entry in data]
        
        # Make the trace
        fig.add_scatter(x=timestamps, y=usedSpace, mode="lines", line=dict(color="Blue"), marker=dict(size=5), 
                        name="Disk " + disks[i][-4:] + " Used Space", legendgroup="Disk " + disks[i][-4:], row=i+1, col=1)
        fig.add_scatter(x=timestamps, y=capacity, mode="lines", line=dict(color="Red", dash="dash"), marker=dict(size=5), 
                        name="Disk " + disks[i][-4:] + " Capacity", legendgroup="Disk " + disks[i][-4:], row=i+1, col=1)

        # Update y-axis label
        fig.update_yaxes(title_text="Disk Space for " + disks[i][-4:] + " (GB)" , row=i+1, col=1)

        fig.update_xaxes(
            title_text="Time",
            tickformat="%b %d %H:%M",
            range=[min(timestamps), max(timestamps)],
            fixedrange=True,
            rangeslider=dict(
                visible=True,
                thickness=0.1
            ),
            matches="x",
            type='date',
            row=i+1, 
            col=1
        )
        
        fig.add_pie(labels=['Used Space (GB)', 'Available Space (GB)'], 
            values=[usedSpace[-1], availSpace[-1]],
            row=i+1, col=2,
            marker_colors=['#8b0a1a', '#32cd32'],  # Set the colors
            hoverinfo='label+value+percent',  # Display the percentage on hover
            textinfo='label+value+percent',  # Display the percentage on the chart
            textposition='inside',  # Position the text inside the pie
            showlegend=False,  # Hide the legend
            hole=.1,
            # pull=[0.1, 0.1],  # Explode the pie chart
            domain=dict(x=[0, 1], y=[0, 1])   # Adjust the domain to make the pie chart bigger
        )  
        
        

    # Update layout
    fig.update_layout(
        title_text="System Monitoring Dashboard - Disk Usage",
        title_font_size=30,
        title_x=0.5,
        title_y=0.98,
        title_xanchor="center",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.15,
            xanchor="left",
            x=0.15
        ),
        template="plotly_dark",
        height=700,
        hovermode="x unified",
        autosize=True,
        plot_bgcolor='rgba(20, 20, 20, 0.5)',  # Set the plot background color to a semi-transparent white
    )
    
    
    
    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=24, label="1-day", step="hour", stepmode="backward"),
                dict(count=120, label="5-day", step="hour", stepmode="backward"),
                dict(label="All", step="all")
            ]),
            bgcolor="rgba(255, 255, 255, 0.5)",  # Change the background color of the range selector
            font=dict(color="black"),   # Change the text color of the range selector buttons
            y=1.05
        ),
        row=1,
        col=1,
    )

    if __name__ == "__main__":

        config = {'displaylogo': False} # Config information

        fig.show(renderer="browser", config=config) # Overriding the default renderer

    else:
        return fig


    


if __name__ == "__main__":
    # runspace
    t2 = datetime.now()
    t1 = (t2 - timedelta(days=15)).strftime("%Y-%m-%d %H:%M:%S")
    
    plotData(grabData(t1, t2.strftime("%Y-%m-%d %H:%M:%S")))