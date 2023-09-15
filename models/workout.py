from app import db
from sqlalchemy.orm import relationship

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    completed = db.Column(db.Boolean)
    # exercises = relationship(secondary="Workout_exercise", back_populates="workouts")
    exercises = db.relationship("Exercise", secondary="workout_exercise", backref="workouts")

    def __repr__(self):
        return f"Workout: {self.id}: {self.name}"
    
    # primary is model to access, secondary is what you're accessing it through