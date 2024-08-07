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

@app.route('/')
def index():
    # Generate the Plotly plots
    cpu_plot = plotlyCPU.plotData(plotlyCPU.grabData(t1c_m, t2c_m)).to_html(full_html=False)
    memory_plot = plotlyRAM.plotData(plotlyRAM.grabData(t1c_m, t2c_m)).to_html(full_html=False)
    network_plot = plotlyNETWORK.plotData(plotlyNETWORK.grabData(t1d_n, t2d_n)).to_html(full_html=False)
    disk_plot = plotlyDISK.plotData(plotlyDISK.grabData(t1d_n, t2d_n)).to_html(full_html=False)
    combined_plot = combinedPlot.plot(t1d_n, t2d_n).to_html(full_html=False)

    # Render the index.html template with the plots
    return render_template('index.html', cpu_plot=cpu_plot, memory_plot=memory_plot,  disk_plot=disk_plot, network_plot=network_plot, combined_plot=combined_plot)

# @app.route('/hello/<string:name>')
# def hello(name):
#     return f"Hello, {name}!"

# @app.route('/data', methods=['POST'])
# def data():
#     received_data = request.form.get('data')
#     return f"Received data: {received_data}"

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
