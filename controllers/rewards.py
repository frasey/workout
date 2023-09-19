from flask import Blueprint, render_template, request, redirect
from app import db
from models.rewards import Reward

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

# @rewards_blueprint.route("/exercise/<id>/edit")
# def edit_reward(id):
#     exercise = Exercise.query.get(id)
#     return render_template('exercises/edit.jinja', exercise=exercise)

@rewards_blueprint.route("/rewards/delete")
def delete_reward():
    rewards = Reward.query.all()
    
    return render_template("rewards/edit_delete.jinja", rewards=rewards)