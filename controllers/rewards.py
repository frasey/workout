from flask import Blueprint, render_template, request, redirect
from app import db
from models.rewards import Reward
# should probs call this file rewards_controller to keep consistant naming
rewards_blueprint = Blueprint("/rewards", __name__)

@rewards_blueprint.route("/rewards")
def show_rewards():
    rewards = Reward.query.all()
    return render_template("rewards/add_show.jinja", rewards=rewards)

@rewards_blueprint.route("/rewards", methods=['POST'])
def add_reward():
    name = request.form["reward"]
    new_reward = Reward(name=name)
    db.session.add(new_reward)
    db.session.commit()

    return redirect("/rewards")

@rewards_blueprint.route("/rewards/delete")
def show_deletable_rewards():
    rewards = Reward.query.all()
    return render_template("rewards/edit_delete.jinja", rewards=rewards)

@rewards_blueprint.route("/rewards/delete/<id>", methods={'POST'})
def delete_reward(id):
    reward = Reward.query.get(id)
    db.session.delete(reward)
    db.session.commit()
    return redirect("/rewards/delete")