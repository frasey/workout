from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout import Workout
from models.exercise import Exercise
from models.workout_exercise import Workout_exercise
from models.user import User

workout_blueprint = Blueprint("/workout", __name__)

# Homepage - choose workout
@workout_blueprint.route("/workout", methods=['GET'])
def all_workouts():
    workouts = Workout.query.all()
    args = request.args
    workout = args.get("workout")
    
    print("workout: ",workout)

    if workout:
        workout_to_show = Workout.query.get(workout)
        return render_template("index.jinja", workouts=workouts, workout=workout_to_show)
    else:
        return render_template("index.jinja", workouts=workouts, workout=workout)

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
    return redirect(f"/workout/{workout_id}")

# delete workout
@workout_blueprint.route("/workout/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout = Workout.query.get(id)
    db.session.delete(workout)
    db.session.commit()
    return redirect("/workout/all-workouts")

# workout completed
@workout_blueprint.route("/workout/<id>/workout-completed", methods=['POST'])
def workout_completed(id):
    workout = Workout.query.get(id)
    workout.completed = True

    # if workout_completed:
    #     user = User.query.all()
    #     print("user info:", user)
    #     points = user.points + 1
    #     db.session.add(points)
    #     db.session.commit()     
    return redirect("/workout")


