from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout
from models.exercise import Exercise
from models.workout_exercise import Workout_exercise
from models.user import User
from models.rewards import Reward
from services.workout_services import is_exercise_in_workout
import random

workout_blueprint = Blueprint("/workout", __name__)

# Homepage - choose workout
@workout_blueprint.route("/workout", methods=['GET'])
def all_workouts():
    workouts = Workout.query.all()
    args = request.args
    workout = args.get("workout")
    if workout:
        workout_to_show = Workout.query.get(workout)
        return render_template("index.jinja", workouts=workouts, workout=workout_to_show) #reward=None
    else:
        return render_template("index.jinja", workouts=workouts, workout=workout) #reward=reward

# show one workout
@workout_blueprint.route("/workout/<id>")
def show_workout(id):
    workout = Workout.query.get(id)
    return render_template("workouts/show_workout.jinja", workout=workout)

# create workout
@workout_blueprint.route("/workout/new")
def new_workout():
    workouts = Workout.query.all()
    return render_template("workouts/new_workout.jinja", workouts=workouts)

# add new workout to db
@workout_blueprint.route("/workout/new", methods=['POST'])
def add_workout():
    name = request.form["name"]
    type = request.form["type"]
    new_workout = Workout(name=name, type=type)
    db.session.add(new_workout)
    db.session.commit()
    return redirect(f"/workout/{new_workout.id}/add-exercises")

# add exercises to workout.id
@workout_blueprint.route("/workout/<id>/add-exercises")
def add_exercises_to_workout(id):
    workout = Workout.query.get(id)
    exercises_to_choose = Exercise.query.all()
    return render_template("workouts/add_exercises.jinja", exercises=exercises_to_choose, workout=workout)

# we can consider extracting out logic and extra verbosity from our controller functions, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see below for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application.
# update db with new workout_exercise
@workout_blueprint.route("/workout/<int:id>/add-exercises", methods=["POST"])
def add_workout_to_db(id):    

    is_key_present= "selected" in request.form
    if is_key_present:
        exercise_ids = request.form.getlist("selected")
    # should prob call 'value' something more descriptive.  
    for value in exercise_ids:
        exercise_id=int(value)
        if Workout_exercise.query.filter(Workout_exercise.exercise_id == value, Workout_exercise.workout_id == id).count() == 0:
            new_workout_exercise = Workout_exercise(exercise_id=exercise_id, workout_id=id)
            db.session.add(new_workout_exercise)
            db.session.commit()

    workout_id = id
    return redirect(f"/workout/{workout_id}")
##########################
# example of howe we might extract code 
###########################


@workout_blueprint.route("/workout/<int:id>/add-exercises", methods=["POST"])
def add_workout_to_db(id):    
    workout_id = id
    is_key_present= "selected" in request.form
    if is_key_present:
        exercise_ids = request.form.getlist("selected")
    for exercise_id in exercise_ids:
        if is_exercise_in_workout(exercise_id, workout_id):
            new_workout_exercise = Workout_exercise(exercise_id=exercise_id, workout_id=workout_id)
            db.session.add(new_workout_exercise)
            db.session.commit()
    
    return redirect(f"/workout/{workout_id}")
# we now have some code that is a lot more human readable, if someone wants/needs to know how it's exactly implemented they are able to do so by looking it the file. we generally want to have less logic inside our controllers as it's not really their job. 

# show all workouts
@workout_blueprint.route("/workout/all-workouts")
def show_all_workouts():
    workouts = Workout.query.all()
    return render_template('workouts/all-workouts.jinja', workouts=workouts)

# edit workout
@workout_blueprint.route("/workout/<id>/edit")
def edit_workout(id):
    workout = Workout.query.get(id)
    exercises = Exercise.query.all()
    return render_template('workouts/edit.jinja', workout=workout, exercises=exercises)

# update workout
@workout_blueprint.route("/workout/<int:id>/edit", methods=["POST"])
def update_workout_in_db(id):    
    name = request.form["name"]
    type = request.form["type"]

    workout = Workout.query.get(id)

    workout.name = name
    workout.type = type
    
    db.session.commit()

    return redirect(f"/workout-exercise/{id}/edit")

# remove exercise from workout
@workout_blueprint.route("/workout/<int:workout_id>/remove/<int:exercise_id>", methods=['POST'])
def remove_exercise_from_workout(workout_id, exercise_id):
    # FILTER BY WORKOUT ID, THEN EXERCISE
    current_workout_exercise = Workout_exercise.query.filter(Workout_exercise.workout_id == workout_id, Workout_exercise.exercise_id == exercise_id).one()
    db.session.delete(current_workout_exercise)
    db.session.commit()
    return redirect(f"/workout/{workout_id}/edit")

# delete workout
@workout_blueprint.route("/workout/<id>/delete", methods=['POST'])
def delete_workout(id):
    Workout_exercise.query.filter(Workout_exercise.workout_id == id).delete()
    workout = Workout.query.get(id)
    db.session.delete(workout)
    db.session.commit()
    return redirect("/workout/all-workouts")

# workout completed
@workout_blueprint.route("/workout/<id>/workout-completed", methods=['POST'])
def workout_completed(id):
    workout = Workout.query.get(id)
    workout.completed = True
    reward_value = 1
    User.query.all()
    user = User.query.filter(User.id >= 0).one()

    if workout.completed:
        user.points += reward_value
        db.session.commit()
    return redirect("/workout/reward")

@workout_blueprint.route("/workout/reward")
def output_reward():
    rewards = Reward.query.all()
    reward = random.choice(rewards)
    User.query.all()
    user = User.query.filter(User.id >= 0).one()
    # this code is just checking if the user's points is divideable by 5, if the user has 9 points this will say no reward... I don't know the if this is intentional or not? 
    if user.points %5 ==0:
        return render_template("rewards/output_reward.jinja", reward=reward)
    else:
        return render_template("rewards/no_reward.jinja", user=user)