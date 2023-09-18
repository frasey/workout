from flask import Blueprint
from app import db
from models.rewards import Reward

rewards_blueprint = Blueprint("/rewards", __name__)