from flask import Blueprint, render_template, redirect, request
from app import db
from models.exercise import Exercise
from models.workout import Workout

exercise_blueprint = Blueprint("/exercise", __name__)

# show all exercises
@exercise_blueprint.route("/exercise")
def show_all():
    exercises = Exercise.query.all()
    workouts = Workout.query.all()
    return render_template("exercises/add_new.jinja", exercises=exercises, workouts=workouts)

# edit exercises

# update exercsies

# delete exercise

# add exercise

@exercise_blueprint.route("/exercise/new", methods=['POST'])
def add_new_exercise():
    name = request.form["name"]
    sets = request.form["sets"]
    reps = request.form["reps"]
    new_exercise = Exercise(name=name, sets=sets, reps=reps)

    db.session.add(new_exercise)
    db.session.commit()
    return redirect("/exercise")