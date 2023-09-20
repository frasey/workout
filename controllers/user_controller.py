from flask import Blueprint
from app import db
from models.user import User
from models.rewards import Reward

user_blueprint = Blueprint("/user", __name__)

@user_blueprint.route("/user")
def user_reward():
    User.query.all()
    user = User.query.filter(User.id >= 0).one()
    rewards = Reward.query.all()
    if user.points % 5 == 0:
        if len(user.rewards) >= 1:
            reward = random.choice(rewards)
        pass