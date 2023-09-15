from app import db
# from sqlalchemy.orm import DeclarativeBase, relationship

# class Base(DeclarativeBase):
#     pass

# workout_exercise = Table(
#     "workout_exercise"
#     Base.metadata
#     Column("workout_id", ForeignKey("workouts.id"), primary_key=True)
#     Column("exercise_id", ForeignKey("exercises.id"), primary_key=True)
# )

class Workout_exercise(db.Model):
    __tablename__ = "workout_exercise"

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))