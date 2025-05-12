# Resume-Plus-Portfolio-Builder

## Overview

This project is a Full Stack application built using **React.js** for the frontend and **Django** for the backend. It allows users to create and manage resumes and portfolios.

## Folder Structure

- `frontend/` - React.js frontend application
- `resume_backend/` - Django REST API backend

---

## Frontend (React.js)

### Requirements

- Node.js
- npm or yarn

### Setup Instructions

1. Navigate to the `frontend/` folder:

    ```bash
    cd frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

    or if using yarn:

    ```bash
    yarn install
    ```

3. Run the development server:

    ```bash
    npm start
    ```

    or

    ```bash
    yarn start
    ```

    The frontend will be available at: `http://localhost:3000`

---

## Backend (Django)

### Requirements

- Python 3.x
- MySQL or SQLite
- Django 5.2.1
- Django REST framework
- MySQLdb (for MySQL)

### Setup Instructions

1. Navigate to the `resume_backend/` folder:

    ```bash
    cd resume_backend
    ```

2. Set up a Virtual Environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **Windows**: `venv\Scripts\activate`
    - **macOS/Linux**: `source venv/bin/activate`

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. (Optional) Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the server locally:

    ```bash
    python manage.py runserver
    ```

    The API will be available at: `http://127.0.0.1:8000`

---

## API Endpoints (Backend)

- **GET** `/api/resumes/` - List all resumes
- **POST** `/api/resumes/` - Create a new resume
- **GET** `/api/resumes/{id}/` - Get a resume by ID
- **PUT** `/api/resumes/{id}/` - Update a resume by ID
- **DELETE** `/api/resumes/{id}/` - Delete a resume by ID

---

## Requirements

### Backend (`requirements.txt`)
Django==5.2.1
djangorestframework==3.14.0
mysqlclient==2.1.1


To generate it:

bash
pip freeze > requirements.txt

"dependencies": {
  "react": "^17.0.2",
  "react-dom": "^17.0.2",
  "react-scripts": "4.0.3",
  "axios": "^0.21.1"
}

This README.md file is a combined guide for setting up both the frontend and backend parts of your project. It includes setup instructions, required dependencies, and deployment details for both React and Django.



