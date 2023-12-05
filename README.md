# SDET-Coding-Challenge
A coding project based on webscraping and testing on http://sdetchallenge.fetch.com/

Objective: Using a balance scale and a set of gold coins, identify the counterfeit gold coin among them. All genuine coins have identical weight, while the fraudulent one is lighter than the authentic ones.

## Table of contents
- [Prerequisites](#Prerequisites)
- [Setup](#Setup)
- [Troubleshooting](#Troubleshooting)
- [Usage](#Usage)

## Prerequisites

In order for the solution script to find the fake gold, the following must be installed onto your machine:

* Google chrome browser
* Python

## Setup

To get started with this project, make sure you have `pipenv` installed. This will allow the program to set up a virtual environment and install any needed dependencies. If you don't have `pipenv` yet, please follow the appropriate installation instructions depending on your operating system in the terminal:

```
## Windows:
  $ pip install pipenv

## MacOS
  $ brew install pipenv
```

Clone the project repository and cd into the saved directory path. Then, set up the virtual environment and install dependencies by running the following shell commands (recommended):

```
  $ pipenv shell 
  $ pipenv sync
```

Alternatively, if you do not prefer to use a virtual environment, a `requirements.txt` file is provided in the project directory for installing required dependencies:
```
  $ pip3 install -r requirements.txt
```

Now, you are ready to execute the script and process the solution. Run the following commands based on your operating system: 

```
## Windows:
  `$ python src/main.py`

## MacOS:
  `$ PYTHONPATH=. python3 src/main.py`
```

Wait for the program to run: the Google Chrome browser will open through Selenium Webdriver, then print the solution in the command line when complete. When finished with the program, simply type the following shell command in project directory to close the virtual environment as needed:

```
  `$ exit`
```

## Troubleshooting:
In the event script is missing modules, set the `PYTHONPATH` to the project's directory. Provided below set the python path to the cloned project directory:

```
## Powershell: 
  $ $Env:PYTHONPATH= "C:\Users\path\to\project\directory\"

## Shell:
  $ export PYTHONPATH="C:\Users\path\to\project\directory\"

## Windows:
  $ setx PYTHONPATH= "C:\Users\path\to\project\directory\"
```

## Usage
This project is for the demonstration and application of python and selenium program to interface with a webpage.
See the Pipfile or requirements.txt for cumulative list of dependencies primarily needed for the scripts to run.
