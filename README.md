# SDET-Coding-Challenge
A coding project based on webscraping and testing on http://sdetchallenge.fetch.com/

## Table of contents
- [Prerequisites](#Prerequisites)
- [Setup](#Setup)
- [Usage](#Usage)

## Prerequisites

* Google chrome browser
* Python

## Setup

This project will also require having pipenv to set up a virtual environment and install dependencies. Install pipenv (if have, skip the following commands):

Windows: `$ pip install pipenv`
MacOS: `$ brew install pipenv`

Clone the repository and cd into the project's saved directory path. 
Set up the virtual environment and install dependencies by running the following shell commands (recommended):

```
  $ pipenv shell 
  $ pipenv sync
```

> Alternatively, a requirements.txt file is provided in the project directory for installing needed dependencies:
>```
>  $ pip3 install -r requirements.txt
>```

Run the following commands 

MacOS: `$ PYTHONPATH=. python3 src/main.py`
Windows: `$ python src/main.py`

Wait for the program to run.
The Google Chrome browser will open through Selenium Webdriver, then finally print the solution in the command line when complete.


> Troubleshooting: In the event script is missing modules, set the PYTHONPATH to the project's directory. Provided below set the python path to the cloned project directory:
>
> Powershell: `$ $Env:PYTHONPATH= "C:\Users\path\to\project\directory\"`
> Shell: `$ export PYTHONPATH="C:\Users\path\to\project\directory\"`
> Windows: `$ setx PYTHONPATH= "C:\Users\path\to\project\directory\"`

When finished, simply type the following command in project directory to close the virtual environment:

```
  `$ exit`
```

## Usage
This project is for the demonstration and application of python and selenium program to interface with a webpage.
See the Pipfile for cumulative list of dependencies primarily needed for the scripts to run.
