# Forum

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.8-brightgreen.svg)](https://djangoproject.com)

I have built this forum application by following vitorfs's tutorial series. For the complete tutorial series index [click here](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).


## Running the Project Locally

First, clone the repository to your local machine:

```bash
https://github.com/shaonsust/Forum.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
