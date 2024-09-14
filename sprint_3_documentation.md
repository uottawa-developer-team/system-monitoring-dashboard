# Sprint 3 Progress Report

## Introduction
**Overview of Sprint 3:**
- Sprint 3 began on July 27th and Concluded on August 14th. The focus of Sprint 3 was to improve and upgrade the visualizations used for the raw data, and to host these on a rendering platform of our choice. These goals were accomplished, going above and beyond using a Flask web app to render the graphs dynamically, with data filtering, scrolling/panning, and multi-plot graph systems.

**Objectives and Goals:**
- Create advanced data visualization plots
- Choose a rendering platform for the graphs
- Set up automatic data gathering system for users
- Test and debug system top-to-bottom
- Document the sprint

## Completed Work
### Task 1: Create advanced data visualization plots
**Description:**
- The plotly python library was used in favour of the more rudimentary matplotlib library due to its greater interactability and end-user appeal.

**Outcomes:**
- Plotly was chosen as the plotting library.
- Created individual plots for each major section of data
- Created combined plot for all data
- Implemented data filtering system to allow 'zoom' using 'sliders'
- Relevant code snippets for plot creation in plotly:
    ```python
    def plotNet(t1, t2, file, figure, row=2, col=2):

    # Grab Data
    data = grabData(t1, t2, file)

    # Extract the timestamps from the data
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

    rx_bytes = [int(entry['network']['rx_bytes'])/(1024**2) for entry in data]
    tx_bytes = [int(entry['network']['tx_bytes'])/(1024**2) for entry in data]
    

    figure.add_bar(x=timestamps, y=rx_bytes, name="Received Bytes", row=row, col=col)
    figure.add_bar(x=timestamps, y=tx_bytes, name="Transmitted Bytes", row=row, col=col)


    figure.update_yaxes(title_text="Network Usage (MB)", row=row, col=col)
    figure.update_xaxes(
        title_text="Time", 
        range=[min(timestamps), max(timestamps)],
        fixedrange=True,
        rangeslider=dict(
            visible=True,
            thickness=0.1
        ),
        row=row, 
        col=col)
    ```

### Task 2: Choose a rendering platform for the graphs
**Description:**
- After experimenting with a Dash application, the benefits of integrating a Flask web app with plotly graphs outweighed the downsides of a web-based rendering system.

**Outcomes:**
- Set up a simple web server using Flask (w/ Python)
- Integrated data visualizations into the Flask app
- Created a detailed scroll-based web application that can be hosted locally by a user to visualize their system's data.
- Example output: ![image](https://github.com/user-attachments/assets/2cee4de1-8274-42cb-8ef6-dd09764727ac)

### Task 3: Set up automatic data gathering system for users
**Description:**
- A system was required for regular, automatic data collection at fixed but differing intervals for each data type. Cron job systems were used to accomplish this, and data storage systems were adjusted to cap out at a maximum line count, to prevent excessive storage.

**Outcomes:**
- Set up scripts to set up or remove a one-hour cron job that triggers data collection periodically
- Created a data collection script that activates all sub-scripts when triggered by the cron job
- Updated the Flask app to refersh every 5 minutes to grab and include latest data
- Integrated system to cull all data beyond a fixed range of lines (1 day for most, 10 days for disk space data)
- Sample code for cron job setup:
    ```bash
    #!/bin/bash
    # Get the absolute path of the populate_variable_data.sh script
    SCRIPT_PATH=$(realpath "$(dirname "$0")/populate_variable_data.sh")
    
    # Check if the script file exists
    if [[ ! -f "$SCRIPT_PATH" ]]; then
        echo "SYSTEM MONITORING DASHBOARD ERROR: Script $SCRIPT_PATH does not exist."
        exit 1
    fi
    
    # Make sure the script is executable
    chmod +x "$SCRIPT_PATH"
    
    # Define the cron job
    CRON_JOB="0 * * * * $SCRIPT_PATH"
    
    # Check if the cron job already exists
    EXISTING_CRON=$(crontab -l 2>/dev/null | grep -F "$SCRIPT_PATH")
    
    if [[ -n "$EXISTING_CRON" ]]; then
        echo "SYSTEM MONITORING DASHBOARD: Cron job already exists."
    else
        # Append the cron job if it doesn't exist
        (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
        if [[ $? -eq 0 ]]; then
            echo "SYSTEM MONITORING DASHBOARD: Cron job added successfully."
        else
            echo "SYSTEM MONITORING DASHBOARD ERROR: Failed to add cron job."
        fi
    fi
    
    # Execute the script once in the background
    "$SCRIPT_PATH" &
    ```

### Task 4: Test and debug system top-to-bottom
**Description:**
- Run a full analysis of all relevant scripts and results, both from the perspectives of an end-user and developper.

**Outcomes:**
- Tested the program start to finish as an end user would
- Tested the program's individual scripts manually to ensure functionality
- Fixed small bugs as they became apparent.

### Task 5: Documentation of the Sprint
**Description:**
- Documented all tasks, outcomes, and processes followed during the sprint.

**Outcomes:**
- Comprehensive documentation created, providing a clear record of the sprint's progress and achievements.

## Achievements
**Key Milestones:**
- Upgraded visualization systems.
- Integrated plots into a Flask web app.
- Set up automatic data collection system.
- Performed final end-to-end testing and debugging.

**Performance Improvements:**
- Capped memory of system to prevent memory leaks or other issues.
- Enhanced visualization capabilities with Plotly.

## Challenges and Issues
### Challenge 1: Dash Application
**Description:**
- Ran into a dead end working on a Dash-based application due to technical constraints and unexpected limitations.

**Mitigation Strategies:**
- Consulted a software QA analysis expert for advice on formatting of the app.
- Redesigned app as a web application in Flask instead, for plotly integration and end-user interactive graphs.

### Challenge 2: Customizing of Visualization
**Description:**
- Customizing the plots on plotly to accomodate the various types of data to be displayed was problematic due to inexperience with the library, and integration with Flask.

**Mitigation Strategies:**
- Studying documentation extensively and tested through trial and error.
- Debugged scripts to ensure accurate data parsing.
- Wrote algorithms to handle dynamic graphs with variable properties, such as the graph for disk space which must accomodate n number of hard drives.

## Lessons Learned
**Positive Outcomes:**
- Learnt how to utilize various libraries and systems such as plotly, Flask, Dash, and cron jobs.
- Improved debugging skills when dealing with complex systems.

**Areas for Improvement:**
- User interface and frontend development.
- Efficiency of data storage.
