import sys
sys.path.append("../visualizations/advanced_visualizations/")
import plotlyCPU # type: ignore
import plotlyRAM # type: ignore
import plotlyNETWORK # type: ignore
import plotlyDISK # type: ignore
import combinedPlot #type: ignore
from flask import Flask, render_template
# from flask import Flask, render_template, request, url_for
from datetime import datetime, timedelta


app = Flask(__name__)

time = datetime.strptime("2024-07-30 19:37:20", "%Y-%m-%d %H:%M:%S")
# Select time for date and time for cpu and memory usage plots
t1c_m = "2024-07-30 19:37:20"
t2c_m = (time + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S")

# Select time for date and time for DISK and Network data
t1d_n = "2024-07-30 19:37:20"
t2d_n = (time + timedelta(minutes=90)).strftime("%Y-%m-%d %H:%M:%S")

# # After setting Up Cron tab
# # Set t1 to 30 minutes before now and t2 to now
# t2 = datetime.now()
# t1 = t2 - timedelta(minutes=30)
# t1_disk = t2 - timedelta(days=2)


# # Convert to string format expected by your plot functions
# t1_str = t1.strftime('%Y-%m-%d %H:%M:%S')
# t2_str = t2.strftime('%Y-%m-%d %H:%M:%S')
# t1_disk_str = t1_disk.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    # Generate the Plotly plots
    cpu_plot = plotlyCPU.plotData(plotlyCPU.grabData(t1c_m, t2c_m)).to_html(full_html=False)
    memory_plot = plotlyRAM.plotData(plotlyRAM.grabData(t1c_m, t2c_m)).to_html(full_html=False)
    network_plot = plotlyNETWORK.plotData(plotlyNETWORK.grabData(t1d_n, t2d_n)).to_html(full_html=False)
    disk_plot = plotlyDISK.plotData(plotlyDISK.grabData(t1d_n, t2d_n)).to_html(full_html=False)
    combined_plot = combinedPlot.plot(t1c_m, t2d_n, t1d_n).to_html(full_html=False)

    # # Generate the Plotly plots
    # cpu_plot = plotlyCPU.plotData(plotlyCPU.grabData(t1_str, t2_str)).to_html(full_html=False)
    # memory_plot = plotlyRAM.plotData(plotlyRAM.grabData(t1_str, t2_str)).to_html(full_html=False)
    # network_plot = plotlyNETWORK.plotData(plotlyNETWORK.grabData(t1_str, t2_str)).to_html(full_html=False)
    # disk_plot = plotlyDISK.plotData(plotlyDISK.grabData(t1_disk_str, t2_str)).to_html(full_html=False)
    # combined_plot = combinedPlot.plot(t1d_n, t2d_n, t1_disk_str).to_html(full_html=False)
    

    # Render the index.html template with the plots
    return render_template('index.html', cpu_plot=cpu_plot, memory_plot=memory_plot,  disk_plot=disk_plot, network_plot=network_plot, combined_plot=combined_plot)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
