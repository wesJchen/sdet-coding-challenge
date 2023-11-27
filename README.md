# sdet-coding-challenge

Project based on webscraping and testing


## table of contents

- [installation](#installation)
- [usage](#usage)

## installation

This project used the pipenv to create a virtual environment in order to install the required modules and packages for setup. Dependencies can be installed in different ways:

1) Set up the virtual environment and install dependencies. (Automatically creates the virtual environment and sets up the dependencies in the pipfile.lock file)

$ pipenv shell

2) A requirements.txt file is provided in the project directory. Simply install all the dependencies:

$ pip install -r requirements.txt

The file will be run through the main.py file in src when the current directory is at the parent level. Using the following command, the user will retrieve the objective of the project.

$ PYTHONPATH=. python3 src/main.py

## usage

This project is for the demonstration and application of python and selenium program to interface with a webpage

