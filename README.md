# sdet-coding-challenge

Coding project based on webscraping and testing

## table of contents

- [installation](#installation)
- [execution](#execution)
- [usage](#usage)

## installation

This project used the pipenv to create a virtual environment in order to install the required modules and packages for setup. Dependencies can be installed in different ways:

For both Mac and windows, install pipenv in the shell (Mac + Windows):

$ pip install pipenv

Next, set up the virtual environment and install dependencies by running the following shell command. This should automatically set up the dependencies found in the pipfile.lock file in a virtual environment. Shell will start up the virtual environment. On Mac, it will display (sdet-coding-challenge):

$ pipenv shell

NOTE: If the dependencies are not installed upon creating the virtual environment, run the following command to install dependencies listed in the Pipfile.lock:

$ pipenv sync

==================================================================================================================================================
Alternatively, a requirements.txt file is provided in the project directory. To install all the dependencies in the file with the following command (However, recommended to be run in the virtual environment instead of using pip installing dependencies directly onto the local environments):

$ pip install -r requirements.txt


## execution

In order to execute the solution, run the main.py script. The pythonpath must be set before the script will proceed.

On Macbook, run the following command in the terminal:
$ PYTHONPATH=. python3 src/main.py


For Windows, run the following command to set the PYTHONPATH to the project's directory:

Powershell example:
$ $Env:PYTHONPATH= = "C:\Users\path\to\project\directory\"

Shell example:
$ export PYTHONPATH="C:\Users\path\to\project\directory\"

Windows example:
$ setx PYTHONPATH= "C:\SyAutomation\automation-tests\ZProjects"


## usage

This project is for the demonstration and application of python and selenium program to interface with a webpage.
See the Pipfile for cumulative list of dependencies primarily needed for the scripts to run.

