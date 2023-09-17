from app import db

class Rewards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))