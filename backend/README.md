# backend aplication - Django rest API
This backend application runs as a REST API, it uses python's Django framework and you must have installed at your local
environment Python 3 (version  >= 3.8.x) and Pip (python's package manager).

## Python virtual environment:
Font - https://docs.python.org/3/library/venv.html

at your bash / zsh terminal run:
Activate - ```$ source ./venv/bin/activate```
Deactivate -  ```$ deactivate```

## Instalation:
at your bash / zsh terminal run:
```$ pip install -r requirements.txt```

## How to run this app:

### Verify if you have mysqlclient installed:
If mysqlclient install fail, please follow the official tutorial for it:
'https://pypi.org/project/mysqlclient/'

```$ export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags` && export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs` && pip install mysqlclient```

### Start up database
Make a mysql DB as described in your Django settings.py in "DATABASES"

## Open DB at terminal
On mac or linux
```mysql -u one_api_admin -p```
At prompt fill the password for this user, remember I already make one at Django settings.py file at "DATABASES" config.
Now you should be running the mysql service for this DB and will be able to connect to it with Django.

### Create a new superuser

### Run development server