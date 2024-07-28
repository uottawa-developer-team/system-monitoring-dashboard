# Sprint 2 Progress Report

## Introduction
**Overview of Sprint 1:**
- Sprint 2 began on July 15th and Concluded on July 21st. The focus of Sprint 2 was to finalize plans of storing the collected data in sprint 1 and to develop initial visualization scripts for the given data. These goals were acheived, The JSON storage format was decided on and four visualisation scripts were written in Python using the Matplotlib library.

**Objectives and Goals:**
- Choose a format for storing collected data 
- Establish a directory structure.
- Modify BASH scripts to store data in chosen format.
- Write initial visualization scripts for all collected data.
- Perform Integration tests of stored data with visualization scripts.
- Documentation of the sprint

## Completed Work
### Task 1: Choose a Format for Storing Collected Data
**Description:**
- Decided on a standardized format for storing collected data, ensuring consistency and ease of access.

**Outcomes:**
- JSON was chosen as the storage format for its simplicity and compatibility with Python.
- Relevant code snippets for JSON creation in BASH:
    ```bash
    create_json(){
        json=$(jq -n \
            --arg timestamp "$timestamp"\
            --arg cpu_data "$cpu_data"\
            '{
                timestamp: $timestamp,
                cpu: {
                    user: ($cpu_data | split(" ")[0]),
                    system: ($cpu_data | split(" ")[1]),
                    nice: ($cpu_data | split(" ")[2]),
                    idle: ($cpu_data | split(" ")[3]),
                    wait: ($cpu_data | split(" ")[4]),
                    hi: ($cpu_data | split(" ")[5]),
                    si: ($cpu_data | split(" ")[6]),
                    st: ($cpu_data | split(" ")[7])
                }
            }')
        echo "$json"
    }
    ```

### Task 2: Establish a Directory Structure
**Description:**
- Created a clear and organized directory structure for storing scripts, data logs, and visualization outputs.

**Outcomes:**
- Directory structure:
    ```
    /project
    ├── /scripts
    │   ├── collect_cpu_usage.sh
    │   ├── collect_disk_usage.sh
    │   ├── collect_memory_usage.sh
    │   └── collect_network_usage.sh
    |   
    ├── /data
    │   ├── cpu_usage.json
    │   ├── disk_usage.json
    │   ├── memory_usage.json
    │   └── cpu_usage.log
    |
    ├── /json_datalog
    │   ├── cpu_usage.json
    │   ├── disk_usage.json
    │   ├── memory_usage.json
    │   └── network_usage.json
    |
    └── /visualizations
        ├── cpu_usage_plot.py
        ├── disk_usage_plot.py
        ├── memory_usage_plot.py
        └── network_usage_plot.py
    ```

### Task 3: Modify BASH Scripts to Store Data in Chosen Format
**Description:**
- Updated existing BASH scripts to store data in JSON format.

**Outcomes:**
- Successfully modified `collect_cpu_usage.sh`, `collect_memory_usage.sh`, `collect_disk_usage.sh`, and `collect_network_usage.sh` to output data in JSON format.
- Example of `collect_cpu_usage.sh` output JSON:
    ```json
    {
        "timestamp": "2023-07-21 14:35:00",
        "cpu": {
            "user": "28.9",
            "system": "10.0",
            "nice": "0.0",
            "idle": "57.8",
            "wait": "3.3",
            "hi": "0.0",
            "si": "0.0",
            "st": "0.0"
        }
    }
    ```

### Task 4: Write Initial Visualization Scripts for All Collected Data
**Description:**
- Developed Python scripts using Matplotlib to visualize the collected data.

**Outcomes:**
- Created initial plots for CPU and memory usage.
- Example code snippet for CPU usage plot:
    ```python
    import json
    import matplotlib.pyplot as plt

    with open('../json_datalog/cpu_usage.json') as f:
        data = [json.loads(line) for line in f]

    timestamps = [entry['timestamp'] for entry in data]
    user_cpu = [float(entry['cpu']['user']) for entry in data]
    system_cpu = [float(entry['cpu']['system']) for entry in data]

    plt.plot(timestamps, user_cpu, label='User CPU')
    plt.plot(timestamps, system_cpu, label='System CPU')
    plt.xlabel('Timestamp')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    plt.show()
    ```

### Task 5: Perform Integration Tests of Stored Data with Visualization Scripts
**Description:**
- Conducted tests to ensure that the data collected by the BASH scripts could be accurately visualized by the Python scripts.

**Outcomes:**
- Verified that JSON data could be successfully parsed and visualized.
- Addressed minor issues with data formatting and script compatibility.
- Example of plot for the cpu usage:
<!--![cpu_usage_plot](https://github.com/user-attachments/assets/f85f190b-cfcf-4e0e-be38-d8796f8961e6) -->
<img src="https://github.com/user-attachments/assets/f85f190b-cfcf-4e0e-be38-d8796f8961e6" alt="cpu_plot" width="800"/>

### Task 6: Documentation of the Sprint
**Description:**
- Documented all tasks, outcomes, and processes followed during the sprint.

**Outcomes:**
- Comprehensive documentation created, providing a clear record of the sprint's progress and achievements.

## Achievements
**Key Milestones:**
- Finalized data storage format.
- Established directory structure.
- Developed initial visualization scripts.

**Performance Improvements:**
- Improved data handling efficiency by using JSON format.
- Enhanced visualization capabilities with Matplotlib.

## Challenges and Issues
### Challenge 1: Data Formatting Issues
**Description:**
- Encountered inconsistencies in the data formatting between different scripts.

**Mitigation Strategies:**
- Standardized data collection and storage processes.
- Implemented thorough testing to ensure consistency.

### Challenge 2: Visualization Script Errors
**Description:**
- Initial visualization scripts had errors due to incorrect data parsing.

**Mitigation Strategies:**
- Debugged scripts and ensured accurate data parsing.
- Added error handling to manage unexpected data formats.

## Lessons Learned
**Positive Outcomes:**
- Successfully implemented a standardized data storage format.
- Achieved initial visualization capabilities.

**Areas for Improvement:**
- Improve initial testing to catch formatting issues earlier.
- Enhance documentation for better clarity.