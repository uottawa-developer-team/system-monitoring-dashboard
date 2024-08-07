import sys
sys.path.append("../visualizations/advanced_visualizations") 
from datetime import datetime, timedelta
from dash import Dash, html, dcc # type: ignore
import plotlyCPU # type: ignore
import plotlyRAM # type: ignore
import plotlyNETWORK # type: ignore
import plotlyDISK # type: ignore
# from combinedPlot import plot
import combinedPlot # type: ignore

app = Dash(__name__)

time = datetime.strptime("2024-07-30 19:37:20", "%Y-%m-%d %H:%M:%S")
# Select time for date and time for cpu and memory usage plots
t1c_m = "2024-07-30 19:37:20"
t2c_m = (time + timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S")

# Select time for date and time for DISK and Network data
t1d_n = "2024-07-30 19:37:20"
t2d_n = (time + timedelta(minutes=90)).strftime("%Y-%m-%d %H:%M:%S")

app.layout = html.Div(
    style={'height': '100vh', 'width': '100vw'},
    children=[
        dcc.Tabs([
            dcc.Tab(label='CPU Usage', children=[
                dcc.Graph(
                    id='cpu-usage',
                    figure=plotlyCPU.plotData(plotlyCPU.grabData(t1c_m, t2c_m)),
                    style={'height': '90vh'}
                )
            ]),
            dcc.Tab(label='Memory Usage', children=[
                dcc.Graph(
                    id='memory-usage',
                    figure=plotlyRAM.plotData(plotlyRAM.grabData(t1c_m, t2c_m)),
                    style={'height': '90vh'}
                )
            ]),
            dcc.Tab(label='Disk Usage', children=[
                dcc.Graph(
                    id='disk-usage',
                    figure=plotlyDISK.plotData(plotlyDISK.grabData(t1d_n, t2d_n)),
                    style={'height': '90vh'}
                )
            ]),
            dcc.Tab(label='Network Usage', children=[
                dcc.Graph(
                    id='network-usage',
                    figure=plotlyNETWORK.plotData(plotlyNETWORK.grabData(t1d_n, t2d_n)),
                    style={'height': '90vh'}
                )
            ]),
            dcc.Tab(label='Combined Plots', children=[
                dcc.Graph(
                    id='combined-plots',
                    figure=combinedPlot.plot(t1d_n, t2d_n),
                    style={'height': '90vh'}
                )
            ])
        ])
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, port=8051)