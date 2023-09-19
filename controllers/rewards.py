from flask import Blueprint, render_template, request, redirect
from app import db
from models.rewards import Reward

rewards_blueprint = Blueprint("/rewards", __name__)

@rewards_blueprint.route("/rewards")
def show_rewards():
    rewards = Reward.query.all()
    return render_template("rewards/add_show_rewards.jinja", rewards=rewards)

@rewards_blueprint.route("/rewards", methods=['POST'])
def add_reward():
    name = request.form["reward"]
    new_reward = Reward(name=name)
    db.session.add(new_reward)
    db.session.commit()

    return redirect("/rewards")
