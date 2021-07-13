# django-rest-demo
Creating websites using React and Django REST Framework

# Setting Up 
1. First things first make sure to have a Python virtual environment in place. Create a new folder and move into it:

mkdir django-react && cd $_

2. Once done create and activate the new Python environment:

python3 -m venv venv
source venv/bin/activate

NOTE: from now on make sure to be always in the django-react folder and to have the Python environment active.

3. Now let's pull in the dependencies:

pip install django djangorestframework

When the installation ends you're ready to create a new Django project:

django-admin startproject django_react .

