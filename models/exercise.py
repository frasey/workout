from app import db
from sqlalchemy.orm import relationship

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    # workouts = db.relationship(secondary="workout_exercise", back_populates="exercises")
    # workout_exercises = db.relationship("Workout", secondary="Workout_exercise", backref="exercises")

    def __repr__(self):
        return f"Exercise: {self.id}: {self.name}"
    