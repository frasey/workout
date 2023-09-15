from flask import Flask
from flask_sqlalchemy import SQAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eileinfraser@localhost:5432/workout"
db = SQAlchemy(app)
migrate = Migrate(app.db)