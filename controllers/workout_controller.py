from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout

workout_blueprint = Blueprint("/workout", __name__)

# Homepage - choose workout, mark completed
@workout_blueprint.route("/workout")
def all_workouts():
    workouts = Workout.query.all()
    return render_template("index.jinja", workouts=workouts)

# create workout

# edit workout

# delete workout

