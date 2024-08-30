System Monitoring Dashboard

Project Description:
The System Monitoring Dashboard is a tool designed to monitor and visualize system performance metrics such as CPU usage, memory usage, disk space, and network activity. The project uses Bash scripts for data collection and Python with Flask for data visualization and creating an interactive web-based dashboard.

Features:
- Real-time monitoring of system performance metrics
- Data collection using Bash scripts
- Data visualization using Python
- Interactive web-based dashboard using Flask
- Historical data analysis

Technologies Used:
- Python
- Bash
- Flask
- Matplotlib
- Plotly

Package Structure:
- smd_package_linux/
  - README.md              # Package documentation
  - LICENSE                # License 
  - setup                  # Script to setup cron
  - run                    # Script to run the visualization
  - remove                 # Script to remove cron
  - .processes             # Packaged visualization scripts and dependencies



1. **Setup Cron**  
   Navigate to the `smd_package_linux` directory and execute the setup script to set up cron for data collection. This script will automatically run the data collection scripts at scheduled intervals.

   ```
   cd smd_package_linux
   ./setup
   ```

   Wait 10-30 minutes for data to be collected.

2. **Run the Dashboard**  
   Run the dashboard by executing the `run` script. This will start a Flask web server to serve the dashboard.

   ```
   ./run
   ```

   After running the command, access the dashboard by opening a web browser and navigating to `http://127.0.0.1:8429`.

3. **Remove Cron Job**  
   To stop the cron job for data collection, execute the `remove` script.

   ```
   ./remove
   ```

4. **Delete the Directory**  
   To completely remove the System Monitoring Dashboard, navigate to the parent directory of `smd_package_linux` and delete the directory and all its contents.

   ```
   cd ..
   rm -rf smd_package_linux/
   ```

License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

Contacts
- Project Manager: Hezekiah Shobayo (ishob080@uottawa.ca), Adam Norris (anorr029@uottawa.ca)
- Developers: Hezekiah Shobayo, Adam Norris
