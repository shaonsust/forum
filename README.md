# Forum

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.8-brightgreen.svg)](https://djangoproject.com)

I have built this forum application by following vitorfs's tutorial series. For the complete tutorial series, please [click here](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).


## Clone the Project From github

First, clone the repository to your local machine:

```bash
https://github.com/shaonsust/Forum.git
```

## Running the project locally by project_setup.sh

First go to project's root folder where manage.py file is exist. Run the following command to setup the project locally:

```bash
/bin/bash project_setup.sh
```

## Or Running the project locally by following steps:

* Go to project's root folder where manage.py file is exist. Then run the following command to create virtual environment:

```bash
python3.8 -m venv venv
```

* Activate virtual environment by running following command:
```bash
source venv/bin/activate
```

* Install the requirements:

```bash
pip install -r requirements.txt
```

* Setup the local configurations:

```bash
cp .env.example .env
```

* Create the database:

```bash
python manage.py migrate
```

* Load some initial data:

```bash
python manage.py loaddata initial_data.json
```

* Create a super user:

```bash
python manage.py createsuperuser
```

* Finally, run the development server:

```bash
python manage.py runserver
```

* The project will be available at **127.0.0.1:8000**.

To run the project every time after setup, you must first activate the virtual environment and then run the server by following two command:

```bast
source venv/bin/activate
python manage.py runserver
```
