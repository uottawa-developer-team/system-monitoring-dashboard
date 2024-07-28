from matplotlib import pyplot as plt, dates as mdates # type: ignore
import json
from datetime import datetime, timedelta

FILEPATH = "../../json_datalog/disk_data.json"

# Function to grab data form data file
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

# Function to format the plot(s)
def formatPlot(plot=plt, xlabel="", ylabel="", title="", legend_loc="upper left", grid=True, dformat='%H:%M:%S'):
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)
    plot.set_title(title)
    plot.legend(loc=legend_loc)
    plot.grid(grid)
    plot.xaxis.set_major_formatter(mdates.DateFormatter(dformat))


def plotData(data):

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    # Find the name of disk(s)
    disks = [ data[0]['disk'][i]['device'] for i in range (len(data[0]['disk']))]

    # Sort the disk(s) name(s)
    disks = sorted(disks)

    # Use the length to determine the number of disks
    numOfDisks = len(disks)

    fig, axs = plt.subplots(numOfDisks,2, figsize=(13, 7))
    plt.gcf().canvas.manager.set_window_title('System Monitoring Dashboard - Disk Usage')
    

    for i in range(numOfDisks):

        # Extract the data for each disk
        capacity = [float(entry['disk'][i]['size'][:-1]) for entry in data]
        availSpace = [float(entry['disk'][i]['avail'][:-1]) for entry in data]
        usedSpace = [float(entry['disk'][i]['used'][:-1]) 
                     if entry['disk'][i]['used'][-1] == "G" else float(entry['disk'][i]['used'][:-1])/1024 
                     for entry in data]
        
        # Plot the Pie Chart
        axs[numOfDisks-i-1][1].pie([usedSpace[-1], availSpace[-1]], labels=["Used","Available"], autopct='%1.1f%%', shadow=True, startangle=90,
                                                            colors=['r', 'g'], explode=[0.1,0.1])
        

        # Plot the graph 
        axs[i][0].plot(timestamps, capacity, label="Total Size of Disk", color="red", linestyle="--")
        axs[i][0].plot(timestamps, usedSpace, label="Used Space")
        
        # Format the Plot
        formatPlot(axs[i][0], xlabel="Time", ylabel="Disk Space (Gb)", title="Disk " + disks[i][-4:] + " Usage over Time.",dformat="%H:%M")

       

    fig.subplots_adjust(hspace=0.5)
    plt.show()


#runspace
t1 = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d %H:%M:%S")
t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


plotData(grabData(t1, t2))