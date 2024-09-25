# System Monitoring Dashboard

## Project Description
The System Monitoring Dashboard is a tool designed to monitor and visualize system performance metrics such as CPU usage, memory usage, disk space, and network activity. The project leverages Bash for data collection and Python for data visualization, using libraries such as Matplotlib and Plotly to create interactive and informative dashboards.

## Features
- Real-time monitoring of system performance metrics
- Data collection using Bash scripts
- Data visualization using Python (Matplotlib, Plotly)
- Interactive web-based dashboard using Flask
- Historical data analysis

## Technologies Used
- Python
- Bash
- Flask
- Matplotlib
- Plotly

## Getting Started
### Prerequisites
- Python 3.12.3
- Bash
- Browser
- Virtualenv (optional but recommended)
- jq
- pip

### Download
Visit the [System-Monitoring-Dashboard](https://system-monitoring-dashboard.pages.dev/) webpage and download the package specific to your OS, unzip the package and refer to the README for setup instructions

### Setup
1. **Set Up Virtual Environment (optional)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install jq**
   ```bash
   sudo apt install jq
   ```
4. **Setup Cron**
   In the first level of your current directory `smd_package_linux`, run the `setup` script and wait at least 10 minutes before attempting to run the visualization
   ```bash
   ./setup
   ```
### Usage
1. **Run the Dashboard**
   In the first level of your current directory `smd_package_linux`, run the `run` script.
   ```bash
   ./run
   ```
   The plot will automatically open up using your default browser.

2. **Closing the Dashboard**
   To close the dashboard, clost the tab then on your terminal where the local server was run, type in `Ctrl+C` to terminate the process.

### Removal
1. **Removing Cron**
   To remove the cron job, run the `remove` script. You can stop here if you simply want to halt the periodic data collection.

2. **Delete the Directory**
   To delete the directory, navigate to the parent of the `smd_package_linux` and remove the directory and all it's contents using `rm -rf smd_package_linux`

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contacts
- **Project Manager:** [Hezekiah Shobayo: ishob080@uottawa.ca] [Adam Norris: anorr029@uottawa.ca]
- **Developers:** [Hezekiah Shobayo](https://www.linkedin.com/in/hezekiah-shobayo/), [Adam Norris](https://www.linkedin.com/in/adam-j-norris/)


  
## Acknowledgments
- [Python](https://www.python.org/)
- [Bash](https://www.gnu.org/software/bash/)
- [Flask](https://flask.palletsprojects.com/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/)

