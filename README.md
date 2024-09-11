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
  - .venv                  # Directory for virtual environment
  - data/                  # Directory to store collected data
  - json_datalog/          # Directiory to store collected data in JSON format
  - scripts/               # Bash scripts for data collection
  - visualizations/        # Python scripts for data visualization
  - dashboard/             # Flask application for the dashboard
  - smd_package_linux/     # Directory for Linux package
  - smd_package_macos/     # Directory for macOS package
  - webpage/               # Webpage directory for packages download
  - docs/                  # Directory for additional documentation
    - initial_documentaion.md
    - sprint_1_documentation.md
    - sprint_2_documentation.md
    - sprint_3_documentation.md
  - README.md              # Project documentation
  - requirements.txt       # Required Python libraries
  - LICENSE                # License 
```

## Getting Started
### Prerequisites
- Python 3.12.3
- Bash
- Browser
- Virtualenv (optional but recommended)

### Download
Visit the [System-Monitoring-Dashboard](https://system-monitoring-dashboard.pages.dev/) webpage and download the package specific to your OS, unzip the package and refer to the README for setup instructions

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/uottawa-developer-team/system-monitoring-dashboard.git
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
1. **Setup Cron**
   Navigate to the `scripts` directory and execute the Bash script `setup_cron.sh` to collect system performance data and wait 10-30 minutes.
   ```bash
   cd scripts
   ./setup_cron.sh
   ```

2. **Run the Dashboard**
   Navigate to the `dashboard` directory and start the Flask application.
   ```bash
   cd dashboard
   python app.py
   ```

### Demo
https://github.com/user-attachments/assets/fdd25ce1-e03d-4a2c-823a-cae627f0e30c

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


