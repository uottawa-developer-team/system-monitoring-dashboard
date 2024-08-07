import json
from datetime import datetime, timedelta
from plotly.subplots import make_subplots # type: ignore

FILEPATH = "../json_datalog/disk_data.json"


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
    disks = [ data[0]['disk'][i]['device'] for i in range (len(data[0]['disk']))]

    # Sort the disk(s) name(s)
    disks = sorted(disks)

    # Use the length to determine the number of disks
    numOfDisks = len(disks)


    # Create subplots with a mix of 'xy' and 'pie' types
    fig = make_subplots(rows=numOfDisks, cols=2, specs=[[{"type": "xy"}, {"type": "pie"}] for _ in range(numOfDisks)],
                        subplot_titles=[disks[i//2][-4:] if i%2 != 0 else "" for i in range(numOfDisks*2)])


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
        fig.update_xaxes(title_text="Time", row=i+1, col=1)

        
        fig.add_pie(labels=['Used Space (GB)', 'Available Space (GB)'], 
            values=[usedSpace[-1], availSpace[-1]],
            row=i+1, col=2,
            marker_colors=['#8b0a1a', '#32cd32'],  # Set the colors
            hoverinfo='label+value+percent',  # Display the percentage on hover
            textinfo='label+value+percent',  # Display the percentage on the chart
            textposition='inside',  # Position the text inside the pie
            showlegend=False,  # Hide the legend
            # hole=.1)
            pull=[0.1, 0.1])  # Explode the pie chart
        
        

    # Update layout
    fig.update_layout(
        title_text="System Monitoring Dashboard - Disk Usage",
        title_font_size=30,
        title_x=0.5,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_dark",
        height=650,
        autosize=True  # Makes the plot responsive
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
    t1 = (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S")
    t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # specific test case
    # t1 = "2024-07-26 16:07:27"
    # t2 = "2024-07-26 16:38:00"

    FILEPATH = "../../json_datalog/disk_data.json"
    
    plotData(grabData(t1, t2))