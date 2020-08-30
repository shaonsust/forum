#!/bin/bash

create_virtual_environment()
{
    python3.8 -m venv venv
}

activate_virtual_environment()
{
    source venv/bin/activate
}

install_requirements()
{
    pip install -r requirements.txt
}

copy_settings_file()
{
    cp .env.example .env
}

create_database()
{
    python manage.py migrate
}

load_initial_data()
{
    python manage.py loaddata initial_data.json
}

create_super_user()
{
    python manage.py createsuperuser
}

run_server()
{
    python manage.py runserver
}

create_virtual_environment
activate_virtual_environment
install_requirements
copy_settings_file
create_database
load_initial_data
create_super_user
run_server
