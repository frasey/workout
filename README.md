# workout
Solo python project
Using Python, Flask and SQLAlchemy to create a working CRUD app using restful routes. This app is intended to help with executive dysfunction, a trait of ADHD, by giving a reward to help with motivation.

I created an app in which a user can add their own exercises, and add these exercises together to create their own workouts. 
A user can also input their own list of rewards. Completing a workout generates 1 point, and for every 5 points the user is given a random reward from their selection.

Dependencies:

Python 3,
PostgreSQL


Start guide:
```
pip 3 install flask
pip3 install flask-sqlalchemy
pip3 install python-dotenv
pip3 install flask-migrate
pip3 install psychopg2

createdb workout
flask db init
flask run seed
```

In app.py:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_user>@localhost:5432/workout"


To run:
```
flask db upgrade
flask seed
flask run 
```
