# financial_tools

## Installation

### Install Python Libraries

The below instructions will install all the required python packages and libraries to run the application.

```bash
pip3 install -r requirements.txt
```

### Setup .env file

The below instructions will setup the .env file with the required environment variables.

```bash
cp .env.example .env
```

Now edit the .env file to add the required environment variables.

## Usage

Start the server:

```bash
cd FinancialTools
python3 manage.py makemigrations # this will setup the database models
python3 manage.py migrate # this will create the database from the models
python3 manage.py runserver # this runs the server, you can now minimze the console and access the web application
```
