from app import db

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    # using secondary in Workout so don't need to declare relationship twice

    def __repr__(self):
        return f"Exercise: {self.id}: {self.name}"
    