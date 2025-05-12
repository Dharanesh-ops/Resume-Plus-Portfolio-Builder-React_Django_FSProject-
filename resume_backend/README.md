# Resume Backend - Django API

## Overview

This project provides a backend API for managing resumes. It allows users to create, read, update, and delete resumes. The project is built using Django and Django REST Framework.

## Requirements

- Python 3.x
- MySQL or SQLite (configured in `settings.py`)
- Django 5.2.1
- Django REST framework
- MySQLdb (for MySQL)

## Setup Instructions

### 1. Clone the repository

bash
git clone https://github.com/YourUsername/Resume-Plus-Portfolio-Builder-React_Django_FSProject.git
cd resume_backend

2. Set up a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Apply Database Migrations
bash
Copy
Edit
python manage.py migrate
5. Create a Superuser (Optional)
bash
Copy
Edit
python manage.py createsuperuser
6. Run the Server Locally
bash
Copy
Edit
python manage.py runserver
The API will be available at: http://127.0.0.1:8000

API Endpoints
GET /api/resumes/ - List all resumes

POST /api/resumes/ - Create a new resume

GET /api/resumes/{id}/ - Get a resume by ID

PUT /api/resumes/{id}/ - Update a resume by ID

DELETE /api/resumes/{id}/ - Delete a resume by ID

Deployment (Optional)
To deploy the app on Heroku:

Install Heroku CLI and login:

bash
Copy
Edit
heroku login
Create and push the app to Heroku:

bash
Copy
Edit
heroku create
git push heroku master
Set up the database:

bash
Copy
Edit
heroku addons:create heroku-postgresql:hobby-dev
heroku run python manage.py migrate
Create a superuser (optional):

bash
Copy
Edit
heroku run python manage.py createsuperuser
Open the app:

bash
Copy
Edit
heroku open
####Requirements (requirements.txt)
ini
Copy
Edit
Django==5.2.1
djangorestframework==3.14.0
mysqlclient==2.1.1
To generate it:

bash
Copy
Edit
pip freeze > requirements.txt
This README.md file covers setup, usage, and deployment instructions in a more concise form.

arduino
Copy
Edit

This simplified version is a compact yet clear guide for setting up, running, and deploying your 
