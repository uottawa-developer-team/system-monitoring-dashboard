import json
from datetime import datetime, timedelta
from matplotlib import pyplot as plt, dates as mdates # type: ignore

FILEPATH = "../../json_datalog/network_data.json"

def grabData(startDate, endDate):
    with open(FILEPATH, 'rt') as file:
        dataList = json.load(file) # load the file as a list of dicitonaries

    startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S') #define start and end dates of plotted data
    endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')

    croppedData = [entry for entry in dataList if startDate <= datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') <= endDate]

    return croppedData

def plotData(data):

    # Convert data to List
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]
    rxbytes = [int(entry['network']['rx_bytes'])/(1024**2) for entry in data]
    txbytes = [int(entry['network']['tx_bytes'])/(1024**2) for entry in data]


    plt.figure(figsize=(10, 6))
    plt.gcf().canvas.manager.set_window_title('System Monitorng Dashboard - Network')
    plt.plot(timestamps, rxbytes, label='Received Bytes')
    plt.plot(timestamps, txbytes, label='Transmitted Bytes')
    
    
    plt.xlabel('Time')
    plt.ylabel('Bytes (MB)')
    plt.title('Network Data')
    plt.legend()
    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    
    plt.tight_layout()
    plt.show()

t1 = "2024-07-27 23:42:00"
t2 = "2024-07-27 23:53:11"

plotData(grabData(t1, t2))


