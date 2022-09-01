# financial_tools

## Installation

The below instructions will install all the required python packages and libraries to run the application.

```bash
pip3 install -r requirements.txt
```

## Usage

Start the server:

```bash
cd FinancialTools
python3 manage.py makemigrations # this will setup the database models
python3 manage.py migrate # this will create the database from the models
python3 manage.py runserver # this runs the server, you can now minimze the console and access the web application
```
