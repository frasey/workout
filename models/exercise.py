from app import db

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    workout_exercises = db.relationship("Workout_exercise", backref="exercise")

    def __repr__(self):
        return f"Exercise: {self.id}: {self.name}"