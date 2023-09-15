from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout

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

# edit workout

# delete workout

