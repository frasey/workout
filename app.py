from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eileinfraser@localhost:5432/workout"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models and register controllers
from controllers.exercise_controller import exercise_blueprint
from controllers.workout_controller import workout_blueprint
from controllers.workout_exercise_controller import workout_exercise_blueprint
from controllers.user_controller import user_blueprint
from controllers.rewards import rewards_blueprint

app.register_blueprint(exercise_blueprint)
app.register_blueprint(workout_blueprint)
app.register_blueprint(workout_exercise_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(rewards_blueprint)

