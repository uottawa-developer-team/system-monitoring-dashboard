from matplotlib import pyplot as plt, dates as mdates # type: ignore
import json
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

    plt.figure(figsize=(10, 6))
    plt.gcf().canvas.manager.set_window_title('System Monitoring Dashboard - RAM')
    plt.plot(timestamps, totalRam, label="Total RAM", color="red", linestyle="--")
    plt.plot(timestamps, usedRam, label="Used RAM", color="yellow")

    plt.xlabel("Time")
    plt.ylabel("RAM Usage (MB)")
    plt.title("RAM Usage Over Time")
    plt.legend()
    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    plt.tight_layout()
    plt.show()

#runspace
t1 = (datetime.now() - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

plotData(grabData(t1, t2))