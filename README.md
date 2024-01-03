# workout
Solo python project
Using Python, Flask and SQLAlchemy to create a working CRUD app using restful routes. This app is intended to help with executive dysfunction, a trait of ADHD, by giving a reward to help with motivation.

I created an app in which a user can add their own exercises, and add these exercises together to create their own workouts. 
A user can also input their own list of rewards. Completing a workout generates 1 point, and for every 5 points the user is given a random reward from their selection.


# The Project
This was my second solo Python project. I really pleased by how much more easily it came to me the second time around and was able to create a larger app in the same period of time. I knew that I wanted to go with a lo-fi and orange based colour scheme and I liked how it turned out. I made a point of including checkboxes as part of this project, as I had a bit of a block with them initially and was happy to have conquered them. I thought carefully about how to implement the rewards, and decided to leave them so that a user can add duplicates in order to weight rewards as best suits them for what they can have more regularly.


# What would I do differently or like to keep working on
- Rather than a join table I used a secondary relationship for my classes. In some ways this made things easier, but it had an impact on how some outputs have rendered. If I did it again I think I would opt for a normal join table as secondary caused some unexpected complexitites, but for now I would just like to fix where the output is rendering still in sqyare brackets.
- I would like to keep working on the styling of this app as I think it could be better. 


# Project screenshots

|          |           |           |
| -------- | --------- | --------- |
| <img width="340" alt="Homepage" src="https://github.com/frasey/workout/assets/129194569/a8e00dd5-668e-4046-bece-a4650eedc977"> | <img width="340" alt="Choose a workout" src="https://github.com/frasey/workout/assets/129194569/0d973e24-7d0d-4df5-a947-df501124e49c"> | <img width="340" alt="Select and start workout" src="https://github.com/frasey/workout/assets/129194569/82c161ee-f66f-4af9-b44d-a1d8f285b33a"> |
| Homepage | Choose a workout | Select and start workout |
| <img width="340" alt="Add exercise" src="https://github.com/frasey/workout/assets/129194569/bd41a8f1-9531-4e6e-b5ad-c9eb5fecd69f"> | <img width="340" alt="Edit exercise" src="https://github.com/frasey/workout/assets/129194569/881c264e-389e-40d9-90e0-53a8db8d33b3"> | <img width="340" alt="All exercises" src="https://github.com/frasey/workout/assets/129194569/37ab6e1e-c0eb-41ad-9647-a2ecc716fa82"> |
| Add exercise | Edit exercise | All exercises |
| <img width="340" alt="Add a workout" src="https://github.com/frasey/workout/assets/129194569/a8406674-3a0a-47d7-8601-604ead5eaa70"> | <img width="340" alt="Add exercises to workout" src="https://github.com/frasey/workout/assets/129194569/d86bf5e0-d1cf-4f50-812b-590c6a1f01fd"> | <img width="340" alt="Add exercises to workout 2" src="https://github.com/frasey/workout/assets/129194569/34ccdf34-6e3b-459c-938e-bb9888122a90"> |
| Add a workout | Add exercises to workout (1/2)| Add exercises to workout (2/2) |
| <img width="340" alt="New workout" src="https://github.com/frasey/workout/assets/129194569/62c563d3-fdc9-457a-90ea-6459cc3054e0"> | <img width="340" alt="Edit a workout" src="https://github.com/frasey/workout/assets/129194569/f40314af-3bb8-4776-9a52-03ea31085680"> | <img width="340" alt="Edit workout" src="https://github.com/frasey/workout/assets/129194569/e86c3a25-5792-486f-88f5-872bf09bfda0"> | 
| Show new workout | Edit/delete workout| Edit workout (1/2) |
| <img width="340" alt="Edit workout 2" src="https://github.com/frasey/workout/assets/129194569/1fffe343-412d-49be-a296-d99ad0eaa52d"> | <img width="340" alt="workout points" src="https://github.com/frasey/workout/assets/129194569/86ea28d7-9e8a-4390-8fca-2870ac49d6fa"> | <img width="340" alt="rewards" src="https://github.com/frasey/workout/assets/129194569/ef044c7d-32a6-4446-af07-b09848a0f6fb"> |
| Edit workout (2/2) | Workout points | Rewards |
| <img width="340" alt="delete rewards" src="https://github.com/frasey/workout/assets/129194569/b69236d0-4028-4c0e-bc2e-fb6e341b3662"> | <img width="340" alt="workout reward" src="https://github.com/frasey/workout/assets/129194569/b76d2371-3f44-4cb7-8f02-e559bf6ddbfa"> |  |
| Delete reward | Workout reward |  |


Dependencies:
```
Python 3,
PostgreSQL
```

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
