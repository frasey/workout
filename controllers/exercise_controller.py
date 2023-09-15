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
    return render_template("exercises/show_all.jinja", exercises=exercises, workouts=workouts)

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

# edit exercises
@exercise_blueprint.route("/exercise/<id>/edit")
def edit(id):
    exercise = Exercise.query.get(id)
    return render_template('exercises/edit.jinja', exercise=exercise)

# update exercises
@exercise_blueprint.route("/exercise/<id>/edit", methods=['POST'])
def update_exercise(id):
    name = request.form["name"]
    sets = request.form["sets"]
    reps = request.form["reps"]

    exercise = Exercise.query.get(id)

    exercise.name = name
    exercise.sets = sets
    exercise.reps = reps

    db.session.commit()
    return redirect("/exercise")

# delete exercise
@exercise_blueprint.route("/exercise/<id>/delete", methods=['POST'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()
    return redirect("/exercise")