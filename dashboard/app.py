import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../visualizations/advanced_visualizations"))
import plotlyCPU # type: ignore
import plotlyRAM # type: ignore
import plotlyNETWORK # type: ignore
import plotlyDISK # type: ignore
import combinedPlot #type: ignore
from flask import Flask, render_template
# from flask import Flask, render_template, request, url_for
from datetime import datetime, timedelta


app = Flask(__name__)

# After setting Up Cron tab
t2 = datetime.now()
t1 = t2 - timedelta(days=1)
t1_disk = t2 - timedelta(days=10)


# Convert to string format expected by your plot functions
t1_str = t1.strftime('%Y-%m-%d %H:%M:%S')
t2_str = t2.strftime('%Y-%m-%d %H:%M:%S')
t1_disk_str = t1_disk.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    # Generate the Plotly plots
    cpu_plot = plotlyCPU.plotData(plotlyCPU.grabData(t1_str, t2_str)).to_html(full_html=False)
    memory_plot = plotlyRAM.plotData(plotlyRAM.grabData(t1_str, t2_str)).to_html(full_html=False)
    network_plot = plotlyNETWORK.plotData(plotlyNETWORK.grabData(t1_str, t2_str)).to_html(full_html=False)
    disk_plot = plotlyDISK.plotData(plotlyDISK.grabData(t1_disk_str, t2_str)).to_html(full_html=False)
    combined_plot = combinedPlot.plot(t1_str, t2_str, t1_disk_str).to_html(full_html=False)
    

    # Render the index.html template with the plots
    return render_template('index.html', cpu_plot=cpu_plot, memory_plot=memory_plot,  disk_plot=disk_plot, network_plot=network_plot, combined_plot=combined_plot)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run()