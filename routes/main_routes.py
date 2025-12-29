from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.task import Task

main_bp = Blueprint("main", __name__)

@main_bp.route("/dashboard")
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", tasks=tasks)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.route("/profile")
def profile():
    return render_template("profile.html")
