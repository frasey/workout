from flask import Blueprint
from app import db
from models.user import User

user_blueprint = Blueprint("/user", __name__)