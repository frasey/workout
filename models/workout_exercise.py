from app import db

class Workout_exercise(db.Model):
    __tablename__ = "workout_exercise"

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))