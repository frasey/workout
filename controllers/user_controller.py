from flask import Blueprint, render_template
from app import db
from models.user import User
from models.rewards import Reward

user_blueprint = Blueprint("/user", __name__)

# output random reward for 5 points accrued
# @user_blueprint.route("/user")
# def user_reward():
#     User.query.all()
#     user = User.query.filter(User.id >= 0).one()
#     rewards = Reward.query.all()
#     reward_names = []
#     for reward in rewards:
#         reward_names.append(reward.name)
#     if user.points % 5 == 0:
#         if len(user.rewards) >= 1:
#             reward = random.choice(reward_names)
#     return render_template("index.jinja", reward=reward, user=user)