from app import db

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    completed = db.Column(db.Boolean)
    workout_exercises = db.relationship("Workout_exercise", backref="workout")

    def __repr__(self):
        return f"Workout: {self.id}: {self.name}"