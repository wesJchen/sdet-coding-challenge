# SDET-Coding-Challenge
A coding project based on webscraping and testing on http://sdetchallenge.fetch.com/

## Table of contents
- [Installation](#installation)
- [Execution](#execution)
- [Teardown](#teardown)
- [Usage](#usage)

## Installation
This project uses pipenv to create a virtual environment in order to install the required modules and packages for setup. Prerequisites to running this program requires Google Chrome browser, Selenium and Chromedriver packages (which will be installed through pipenv). Dependencies can also be installed the following ways - see the requirements.txt for >=versions required per package.

For both Mac and windows, install pipenv in the shell (MacOS + Windows):

  $ pip install pipenv

MacOS:
  $ brew install pipenv

Next, set up the virtual environment and install dependencies by running the following shell command. These commands also helpset up the needed dependencies found in the pipfile.lock file in the virtual environment.

  $ pipenv shell
  
  $ pipenv sync

Alternatively, a requirements.txt file is provided in the project directory. To install all the dependencies in the file with the following command (However, the recommended flow is to install the dependencies all through the virtual environment instead of using pip installing dependencies directly onto the local environments):

  $ pip install -r requirements.txt


## Execution
To execute, clone the project repository.
Navigate to the project's directory and run the following commands:

MacOS:
$ PYTHONPATH=. python3 src/main.py

Windows:
$ python src/main.py

Wait for the program to run.
The Google Chrome browser will open through Selenium Webdriver, then finally print the solution in the command line when complete.


ADDITIONAL NOTES: The Python Path must be set before the script will proceed. In case the script is not running due to missing modules not found, you may need to set the PYTHONPATH to the project's directory in order for modules in the python path to be imported. Provided below are several ways to set the current python path for the cloned project directory:

Powershell:

  $ $Env:PYTHONPATH= "C:\Users\path\to\project\directory\"
  
Shell:

  $ export PYTHONPATH="C:\Users\path\to\project\directory\"
  
Windows:

  $ setx PYTHONPATH= "C:\Users\path\to\project\directory\"

## Teardown
When finished, simply type the following command in project directory to close the virtual environment:

  $ exit

## Usage
This project is for the demonstration and application of python and selenium program to interface with a webpage.
See the Pipfile for cumulative list of dependencies primarily needed for the scripts to run.
