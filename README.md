Django Project Template with API REST Framework, HTML, Jinja, CSS, and Auto-Upload
This is a template for a Django project with a REST API built using Django REST Framework, HTML templates with Jinja templating engine, CSS for styling, and auto-upload feature

Requirements
Python 3.6 or higher
Django 3.0 or higher
Django REST Framework 3.0 or higher

Installing Space Launch
# Clone this repo and create virtual environment
git clone https://github.com/BulgakovMax/space_launch.git
cd Space_launch

# For Linux/Ubuntu
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt

# For Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Installing with Docker Compose
# Clone this repo and and build docker containers
git clone https://github.com/BulgakovMax/space_launch.git
cd Space_launch

docker compose up --build
Run Space Launch
python manage.py runserver
After starting, you can go to http://127.0.0.1:8000/ and use Space Launch app

Usage
Start the server: python manage.py runserver
Open the browser and navigate to http://localhost:8000 to view the website.
Navigate to http://localhost:8000/api to view the REST API.

Features
Django REST Framework for building RESTful APIs.
HTML templates with Jinja templating engine for dynamic content rendering.
CSS for styling the website.
Auto-upload feature by scripts

Configuration
Django
Change the SECRET_KEY in settings.py to a random string.
Change the ALLOWED_HOSTS in settings.py to the domain name or IP address of your server.
Change the DATABASES in settings.py to use your preferred database engine.

REST Framework
Define your REST API views in api/v1/views.py.
Define your REST API serializers in api/v1/serializers.py.
Define your REST API models in api/v1/models.py.
Define your REST API urls in api/v1/urls.py.

Jinja
Define your HTML templates in templates/.
Use Jinja templating syntax to render dynamic content.

CSS
Define your CSS styles in static/css/.


Author
Developed and maintained by Max Bulgakov.

