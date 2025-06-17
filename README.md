# Ticket-System

A Django-based web application designed to manage and track support tickets efficiently. Built with a modular structure, it offers a user-friendly interface for creating, assigning, and resolving tickets.

## Features

- **User Authentication** — Secure login/logout with Django’s built‑in auth system.
- **Ticket Management** — Create, view, assign, and update ticket records.
- **Admin Dashboard** — View all tickets, filter by status or priority, and manage users.
- **Agent Workflow** — Agents can view only assigned tickets and update statuses.
- **Notification System** (If implemented or future scope) — Email updates or real-time alerts.
- **Responsive UI** — Clean HTML/CSS templates powered by Django’s template engine.

## Tech Stack

- **Backend:** Python, Django  
- **Database:** SQLite (default) — easily switchable to PostgreSQL/MySQL  
- **Frontend:** Django Templates, HTML, CSS  
- **Environments:** `ts_env` virtual environment setup

## Getting Started

### 1. Clone the repository  

git clone https://github.com/ShadminN/Ticket-system.git
cd Ticket-system

## 2. Set up Python virtual environment

python -m venv ts_env

To Activate:

Windows:
ts_env\Scripts\activate

macOS/Linux:
source ts_env/bin/activate

## 3. Install dependencies

pip install -r requirements.txt

## 4. Configure database

By default, Django uses SQLite.
If using a different DB (PostgreSQL/MySQL), update settings.py in Ticketing/TicketingSystem/ accordingly.

## 5. Apply migrations & create superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

## 6. Run the development server

python manage.py runserver

Access the site at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin.

## Future Enhancements
Add email notifications for new or updated tickets

Implement agent role permissions to restrict actions

Enhance frontend with Bootstrap or modern JS frameworks

Add search, export, or analytics functionality


## License
This project is licensed under the MIT License. See LICENSE for details.
