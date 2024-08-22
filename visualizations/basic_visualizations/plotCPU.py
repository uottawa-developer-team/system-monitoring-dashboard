from matplotlib import pyplot as plt, dates as mdates # type: ignore
import json
from datetime import datetime, timedelta
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "../../json_datalog/cpu_usage.json")

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

    # Set the Plotting parameters
    TOTAL_CPU = [100 for datalog in data]
    totalUsepct = [sum([ float(datalog['cpu'][log]) for log in datalog['cpu'] if log != 'idle']) for datalog in data]
    systemPct = [float(datalog['cpu']['system']) for datalog in data]
    userPct = [float(datalog['cpu']['user']) for datalog in data]
    nicePct = [float(datalog['cpu']['nice']) for datalog in data]
    idlePct = [float(datalog['cpu']['idle']) for datalog in data]
    waitPct = [float(datalog['cpu']['wait']) for datalog in data]
    hiPct = [float(datalog['cpu']['hi']) for datalog in data]
    siPct = [float(datalog['cpu']['si']) for datalog in data]
    stPct = [float(datalog['cpu']['st']) for datalog in data]

    # Create figure(s)
    fig, subPlot = plt.subplot_mosaic([['subUses', 'subUses'],
                                    ['totalUse', 'idle']], figsize=(13, 7))
    
    # axs.gcf().canvas.manager.set_window_title('System Monitoring Dashboard - CPU')
    plt.gcf().canvas.manager.set_window_title('System Monitoring Dashboard - CPU')

    # Graph of Subuses
    subPlot['subUses'].plot(timestamps, TOTAL_CPU, label="CPU Capacity", color="red", linestyle="--")
    subPlot['subUses'].plot(timestamps, systemPct, label="System Processes", color="grey")
    subPlot['subUses'].plot(timestamps, userPct, label="User Processes", color="green")
    subPlot['subUses'].plot(timestamps, nicePct, label="Nice Processes", color="pink")
    subPlot['subUses'].plot(timestamps, waitPct, label="Wait", color="orange")
    subPlot['subUses'].plot(timestamps, hiPct, label="Hi(Hardware Interrupts)", color="purple")
    subPlot['subUses'].plot(timestamps, siPct, label="Si(Software Interrupts)", color="brown")
    subPlot['subUses'].plot(timestamps, stPct, label="St(Steal Time)", color="yellow")
    formatPlot(subPlot['subUses'], xlabel="Time", ylabel="CPU Usage (%)", title="CPU Usage - Processes")
               
    
    # Graph of Total CPU Use
    subPlot['totalUse'].plot(timestamps, TOTAL_CPU, label="CPU Capacity", color="red", linestyle="--")
    subPlot['totalUse'].plot(timestamps, totalUsepct, label="Total pct of CPU in use", color="blue")
    formatPlot(subPlot['totalUse'], xlabel="Time", ylabel="CPU Usage (%)", title="CPU Usage - Total")

    
    # Graph of Idle CPU
    subPlot['idle'].plot(timestamps, TOTAL_CPU, label="CPU Capacity", color="red", linestyle="--")
    subPlot['idle'].plot(timestamps, idlePct, label="Total pct of CPU idle", color="black")
    formatPlot(subPlot['idle'], xlabel="Time", ylabel="Idle CPU (%)", title="CPU Usage -Idle")
    
    fig.subplots_adjust(hspace=0.3)
    plt.show()

#runspace
t1 = (datetime.now() - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# specific test case
t1 = "2024-07-18 16:07:19"
t2 = "2024-07-18 16:36:27"

plotData(grabData(t1, t2))