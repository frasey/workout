from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout_exercise import Workout_exercise
from models.workout import Workout

workout_exercise_blueprint = Blueprint("/workout_exercise", __name__)

# route delete (removes a workout from a exercise)
@workout_exercise_blueprint.route("/workout-exercise/<id>/delete", methods=['POST'])
def delete_exercise_from_workout(id):
    # is_key_present= "selected" in request.form
    # if is_key_present == False:
    #     exercise_ids = request.form.getlist("selected")

    # for value in exercise_ids:
    #     exercise_id=int(value)
    # FILTER BY WORKOUT ID, THEN EXERCISE
    current_workout = Workout_exercise.query.filter_by(workout_id = id)
    print("this is the", current_workout)

        # new_workout_exercise = Workout_exercise(exercise_id=exercise_id, workout_id=id)
        # db.session.delete(workout)
        # db.session.commit()

    return redirect(f"/workout-exercise/{workout_id}/edit")

# route creating a new entry (adds a exercise to a workout)
@workout_exercise_blueprint.route("/workout-exercise/<id>/edit")
def show_current_exercises(id):
    workout_id = id
    workout = Workout.query.get(id)
    exercises = Workout_exercise.query.all()

    return render_template("workouts/edit_exercises.jinja", workout_id=workout_id, workout=workout, exercises=exercises)
