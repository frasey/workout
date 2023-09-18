from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout
from models.exercise import Exercise
from models.workout_exercise import Workout_exercise

workout_blueprint = Blueprint("/workout", __name__)

# Homepage - choose workout, mark completed
@workout_blueprint.route("/workout")
def all_workouts():
    workouts = Workout.query.all()
    return render_template("index.jinja", workouts=workouts)

@workout_blueprint.route("/workout", methods=["POST"])
def show_homepage_workout():

    workouts = Workout.query.all()
    return render_template("index.jinja", workouts=workouts)

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
    
    workouts = Workout.query.all()
    workout_id = len(workouts)
    return redirect(f"/workout/{workout_id}/add-exercises")

# add exercises to workout.id
@workout_blueprint.route("/workout/<id>/add-exercises")
def add_exercises_to_workout(id):
    workout = Workout.query.get(id)
    exercises_to_choose = Exercise.query.all()
    return render_template("workouts/add_exercises.jinja", exercises=exercises_to_choose, workout=workout)

# update db with new workout_exercise
@workout_blueprint.route("/workout/<int:id>/add-exercises", methods=["POST"])
def add_workout_to_db(id):    

    is_key_present= "selected" in request.form
    if is_key_present:
        exercise_ids = request.form.getlist("selected")

    for value in exercise_ids:
        exercise_id=int(value)
        new_workout_exercise = Workout_exercise(exercise_id=exercise_id, workout_id=id)
        db.session.add(new_workout_exercise)
        db.session.commit()

    workout_id = id
    return redirect(f"/workout/{workout_id}")

# show all workouts
@workout_blueprint.route("/workout/all-workouts")
def show_all_workouts():
    workouts = Workout.query.all()
    return render_template('workouts/all-workouts.jinja', workouts=workouts)

# edit workout
@workout_blueprint.route("/workout/<id>/edit")
def edit_workout(id):
    workout = Workout.query.get(id)
    return render_template('workouts/edit.jinja', workout=workout)

# update workout


# delete workout
@workout_blueprint.route("/workout/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout = Workout.query.get(id)
    db.session.delete(workout)
    db.session.commit()
    return "deleted"
