# Sprint 4 Progress Report

## Introduction
**Overview of Sprint 4:**
- Sprint 3 began on August 15th and Concluded on August 22nd. The focus of Sprint 4 was to finalize the project package it, and deploy it for end users on Linux platforms. This was accomplished through the use of a [name of platform here] website to host our download page, and pyinstaller to compile the python scripts.

**Objectives and Goals:**
- Package python & bash scripts alongside data storage
- Allow users to interface with application easily
- Deploy a downloadable app as a zip file
- Document the sprint

## Completed Work
### Task 1: Package python & bash scripts alongside data storage
**Description:**
- Pyinstaller was used to package python scripts alongside bash scripts and storage folders

**Outcomes:**
- Pyinstaller was chosen as the main packaging software, producing a single .exe file
- The python scripts were modified to automatically open the web page once the flask app is running
- Multithreading was used to achieve both effects simultaneously
- A zip file was created and added to the GitHub page as a sample download
- Relevant code snippets:
    ```python
    import webbrowser
    import time 
    import threading

    def open_browser():
        time.sleep(3)
        webbrowser.open_new_tab("http://127.0.0.1:8429")
    

    if __name__ == '__main__':
        threading.Thread(target=open_browser).start()
        app.run(port=8429)
    ```

### Task 2: Allow users to interface with application easily
**Description:**
- Added executable files for setting up or uninstalling cron jobs, alongside the main .exe file

**Outcomes:**
- Included 'setup_cron.sh' and 'remove_cron.sh' as files renamed to 'setup.sh' and 'remove.sh'
- Simplified file structure for end users' clarity
- Added a 'README' file containing a user manual and a link to the GitHub page

### Task 3: Deploy a downloadable app as a zip file
**Description:**
- A package folder was prepared containing only necessary files for end users, then deployed as a .zip file

**Outcomes:**
- Simplified file structure in new package folder to end-user-relevant files, including executable files, README, license data, and data storage folders
- Added uncompressed package folder to GitHub page to allow future modifications to the package
- Compresesed package folder and deployed onto the download page

### Task 4: Documentation of the Sprint
**Description:**
- Documented all tasks, outcomes, and processes followed during the sprint.

**Outcomes:**
- Comprehensive documentation created, providing a clear record of the sprint's progress and achievements.

## Achievements
**Key Milestones:**
- Packaged script files with data storage.
- Improved end user app accessbility.
- Deployeed compressed app package.

## Challenges and Issues
### Challenge 1: Using Pyinstaller
**Description:**
- Ran into difficulties when handling complex file structure and varied dependencies when using the pyinstaller tool.

**Mitigation Strategies:**
- Read through the available documentation.
- Explicitly defined package dependencies before using pyinstaller.

### Challenge 2: Opening web page automatically
**Description:**
- Because the Flask app was hosted locally, it was complicated to both open the web page using python and keep the page running simultaneously.

**Mitigation Strategies:**
- Basic multithreading was used to achieve the desired effect.
- A small delay (on the millisecond scale) was used to stagger the opening of the web page.

## Lessons Learned
**Positive Outcomes:**
- Learnt how to use pyinstaller to package a python program.
- Learnt how to effectively deploy an application to end users.

**Areas for Improvement:**
- GUI could be added to prevent user confusion with the various executable files that act as controls.
- A Windows-compatible version could be considered for the project, which would require replacing the BASH scripts.

**Addendum:**
- Developped a modified package version suitable for Mac users.
- Key differences include CPU collection bash script and pyinstaller packaging procedure.
- Deployed new Mac version on the same download page as a compatibility option.