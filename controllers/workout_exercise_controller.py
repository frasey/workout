from flask import Blueprint, render_template, redirect, request
from app import db
from models.workout_exercise import Workout_exercise

workout_exercise_blueprint = Blueprint("/workout_exercise", __name__)