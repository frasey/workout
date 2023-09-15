from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout
from models.exercise import Exercise
from sqlalchemy import desc

workout_blueprint = Blueprint("/workout", __name__)

# Homepage - choose workout, mark completed
@workout_blueprint.route("/workout")
def all_workouts():
    workouts = Workout.query.all()
    return render_template("index.jinja", workouts=workouts)

# @workout_blueprint.route("/workout/<id>")
# def show_workout(id):
#     workout = Workout.query.get(id)
#     return render_template("workouts/show_workout.jinja", workout=workout)



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

    workouts = Workout.query.all()
    workout_id = len(workouts)
    return redirect(f"/workout/{workout_id}/add-exercises")

# add exercises to workout.id
@workout_blueprint.route("/workout/<id>/add-exercises")
def add_exercises_to_workout(id):
    workout = Workout.query.get(id)
    return "working"
# edit workout

# delete workout

