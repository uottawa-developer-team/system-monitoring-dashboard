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

## Package Structure
```
- smd_package_linux/
  - README.md              # Package documentation in markdown
  - README.txt             # Package documentation in text format
  - LICENSE                # License 
  - setup                  # Script to setup cron
  - run                    # Script to run the visualization
  - remove                 # Script to remove cron
  - .processes             # Packaged visualization scripts and dependencies
```
### Usage
1. **Setup Cron**
   Navigate to the `smd_package_linux` directory and execute the Bash script `setup_cron.sh` to set up cron (automatically runs the data collection scripts) and wait 10-30 minutes.
   ```bash
   anon@ymous:~/.../smd_package_linux$ ls
   LICENSE  README.md  remove  run  setup
   anon@ymous:~/.../smd_package_linux$ ./setup 
   SYSTEM MONITORING DASHBOARD: Cron job added successfully.
   ```
2. **Run the Dashboard**
   In the same directory run the `run` script.
   ```bash
   anon@ymous:~/.../smd_package_linux$ ./run
   * Serving Flask app 'app'
   * Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:8429
    Press CTRL+C to quit
   ```
### Deletion or Suspension
1. **Remove Cron**
   Navigate to the `smd_package_linux` directory and execute the Bash script `remove`
   ```bash
   anon@ymous:~/smd_package_linux$ ls
   LICENSE  README.md  remove  run  setup
   anon@ymous:~/smd_package_linux$ ./remove 
   SYSTEM MONITORING DASHBOARD: Cron job removed successfully.
   ```
2. **Delete the Directory**
   Navigate to the parent directory of the `smd_package_linux` then delete the directory and all its contents.
   ```bash
   anon@ymous:~/smd_package_linux$ cd ..
   anon@ymous:~$ rm -rf smd_package_linux/
   ```

## License
This project is licensed under the MIT License. Please take a look at the [LICENSE](LICENSE) file for details.

## Contacts
- **Project Manager:** Hezekiah Shobayo: ishob080@uottawa.ca Adam Norris: anorr029@uottawa.ca
- **Developers:** [Hezekiah Shobayo](https://www.linkedin.com/in/hezekiah-shobayo/), [Adam Norris](https://www.linkedin.com/in/adam-j-norris/)


  
## Acknowledgments
- [Python](https://www.python.org/)
- [Bash](https://www.gnu.org/software/bash/)
- [Flask](https://flask.palletsprojects.com/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/)


