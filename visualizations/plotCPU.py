from matplotlib import pyplot as plt, dates as mdates # type: ignore
import json
from datetime import datetime, timedelta

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

    plt.figure(figsize=(10, 6))
    plt.gcf().canvas.manager.set_window_title('System Monitoring Dashboard - CPU')
    plt.plot(timestamps, TOTAL_CPU, label="CPU Capacity", color="red", linestyle="--")
    plt.plot(timestamps, totalUsepct, label="Culmilative total in Use", color="blue")
    plt.plot(timestamps, systemPct, label="System Processes", color="grey")
    plt.plot(timestamps, userPct, label="User Processes", color="green")
    plt.plot(timestamps, nicePct, label="Nice Processes", color="pink")
    plt.plot(timestamps, idlePct, label="Idle", color="black")
    plt.plot(timestamps, waitPct, label="Wait", color="orange")
    plt.plot(timestamps, hiPct, label="Hi", color="purple")
    plt.plot(timestamps, siPct, label="Si", color="brown")
    plt.plot(timestamps, stPct, label="St", color="yellow")
    

    plt.xlabel("Time")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Usage Over Time")
    plt.legend(loc='upper left')
    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    plt.tight_layout()
    plt.show()

#runspace
t1 = (datetime.now() - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

plotData(grabData(t1, t2))



