from flask import Flask
from flask_sqlalchemy import SQAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eileinfraser@localhost:5432/workout"
db = SQAlchemy(app)
migrate = Migrate(app, db)

# Import models and register controllers
from controllers.exercise_controller import exercise_blueprint
from controllers.workout_controller import workout_blueprint

app.register_blueprint(exercise_blueprint)
app.register_blueprint(workout_blueprint)
