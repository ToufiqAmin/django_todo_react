# Overview

This project is a To Do List web app where users will create, edit and delete their tasks whenever they want using Django and React.

React is a JavaScript framework for developing SPAs (single-page applications). It has solid documentation anda vibrant ecosystem around it.

Django is a Python web framework that simplifies common practices in web development. Django is reliable and also has a vibrant ecosystem of stable libraries supporting common development needs.

For this application, React serves as the frontend, or client-side framework, handling the user interface and getting and setting data via requests to the Django backend, which is an API built using the Django REST framework (DRF).


## Set up and run project locally.
To set up and run, you need to have:
python==3.12.4
node==20.15.0
npm==10.8.1
asgiref==3.8.1
dj-database-url==2.2.0
Django==5.0.6
django-cors-headers==4.4.0
django-heroku==0.3.1
djangorestframework==3.15.2
gunicorn==22.0.0
packaging==24.1
psycopg2==2.9.9
sqlparse==0.5.0
typing_extensions==4.12.2
tzdata==2024.1
whitenoise==6.7.0

Steps:
1. create a folder with the project name
2. create a virtual environment named venv
3. install required versions in both venv and system
4. pull backend and frontend with git in the directory
5. run django and react separately using:
    backend/python manage.py runserver
    frontend/npm start
6. See the project ouput


### API Endpoints
In the projects, I used djangorestframework and django-cors-headers to buit api to interact frontend with the backend. After installing, i added them to the list of installed applications in the settings.py and update the INSTALLED_APPS and MIDDLEWARE sections. And also added some code of the cors-headers to whitelist localhost:3000 because I want the frontend (which will be served on that port) of the application to interact with the API.
After that, I created serializers.py and updated both views.py and urls.py accordingly.
 
