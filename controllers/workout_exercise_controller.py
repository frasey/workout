from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout_exercise import Workout_exercise
from models.workout import Workout

workout_exercise_blueprint = Blueprint("/workout_exercise", __name__)

# route creating a new entry (adds a exercise to a workout)
@workout_exercise_blueprint.route("/workout-exercise/<id>/edit")
def show_current_exercises(id):
    workout_id = id
    workout = Workout.query.get(id)
    exercises = Workout_exercise.query.all()

    return render_template("workouts/edit.jinja", workout_id=workout_id, workout=workout, exercises=exercises)
