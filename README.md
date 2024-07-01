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

## Project Structure
```
- system-monitoring-dashboard/
  - data/                  # Directory to store collected data
  - scripts/               # Bash scripts for data collection
  - visualizations/        # Python scripts for data visualization
  - dashboard/             # Flask application for the dashboard
  - docs/                  # Directory for additional documentation
    - initial_documentaion.md
  - README.md              # Project documentation
  - requirements.txt       # Required Python libraries
```

## Getting Started
### Prerequisites
- Python 3.12.3
- Bash
- Virtualenv (optional but recommended)

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-organization/system-monitoring-dashboard.git
   cd system-monitoring-dashboard
   ```

2. **Set Up Virtual Environment (optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Run Data Collection Scripts**
   Navigate to the `scripts` directory and execute the Bash scripts to collect system performance data.
   ```bash
   cd scripts
   ./collect_cpu_usage.sh
   ./collect_memory_usage.sh
   ./collect_disk_space.sh
   ./collect_network_activity.sh
   ```

2. **Run Data Visualization Scripts**
   Navigate to the `visualizations` directory and execute the Python scripts to generate visualizations.
   ```bash
   cd visualizations
   python visualize_cpu_usage.py
   python visualize_memory_usage.py
   python visualize_disk_space.py
   python visualize_network_activity.py
   ```

3. **Run the Dashboard**
   Navigate to the `dashboard` directory and start the Flask application.
   ```bash
   cd dashboard
   flask run
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contacts
- **Project Manager:** [Hezekiah Shobayo: ishob080@uottawa.ca]
- **Developers:** [Hezekiah Shobayo](https://www.linkedin.com/in/hezekiah-shobayo/), [Adam Norris](anorr029@uottawa.ca)


  
## Acknowledgments
- [Python](https://www.python.org/)
- [Bash](https://www.gnu.org/software/bash/)
- [Flask](https://flask.palletsprojects.com/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/)

