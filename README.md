# Inventory Management System

This is a very simple inventory management system written in django 4 and python 3.10.

## Setup Instructions
- Clone the repository:
    `git clone git@github.com:subodhu/inventory_management.git`
- Change directory:
    `cd inventory_management`
- Make virtual environment:
    `python3 -m venv venv`
- Activate virtual environment:
    `source venv/bin/activate`
- Install dependencies:
    `pip install -r requirements/base.txt`
- Run migrations:
    `python manage.py migrate`
- Add Fixtures:
    `python manage.py loaddata fixtures/inventory.json`
- Run server:
    `python manage.py runserver`

Then visit the [localhost:8000/inventory/](http://localhost:8000/inventory/). You can see the list of inventories.


You can also add new inventory from django admin pannel. For this create a superuser account.
`python manage.py createsuperuser`
Then visit [localhost:8000/admin/](http://localhost:8000/admin/)

You can view the swagger api doc in [localhost:8000/docs/](http://localhost:8000/docs/).
