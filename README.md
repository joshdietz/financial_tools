# Financial Tools - Flask Server

## Description

This is a Flask server that provides a REST API and front-end solution for some financial tools.

## Installation

Install the dependencies:

* Python 3.6 or higher
* Install the required python libraries with `pip3 install -r requirements.txt`
* Configure the environment variables in the `.env` file
  * Create a `.env` file from the `.env.example` file
  * Fill in the values for the environment variables
    * By default, the server will create a 'sqlite' database in the root directory of the project, but this can be changed to postgres by changing the DB_DRIVER environment variable to 'postgres' and filling in the other DB_* variables

## Usage

Run the server with `python3 server.py`. The server will be running on port 5000 by default. 