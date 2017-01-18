# AngularJS + Flask Boilerplate App

A template for building apps with an Angular frontend and a Flask / python backend.

### How to Get Started

1. clone this repo
> https://github.com/shea256/angular-flask

2. install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

3. run the app
> python runserver.py

4. create and seed the db (the server must still be running, so open a new terminal window first)
> python manage.py create_db && python manage.py seed_db --seedfile 'data/db_items.json'
> python manage.py delete_db

5. check out your blog
> http://localhost:5000/blog

6. if you like this project, give it a star :)
