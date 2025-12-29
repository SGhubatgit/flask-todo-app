from flask import Blueprint, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from models.task import Task

task_bp = Blueprint("task", __name__)


# ---------------- ADD TASK ----------------
@task_bp.route("/task/add", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title")

    if not title:
        flash("Task title cannot be empty", "danger")
        return redirect(url_for("main.dashboard"))

    task = Task(
        title=title,
        user_id=current_user.id
    )

    db.session.add(task)
    db.session.commit()

    flash("Task added successfully", "success")
    return redirect(url_for("main.dashboard"))


# ---------------- TOGGLE TASK STATUS ----------------
@task_bp.route("/task/toggle/<int:task_id>")
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash("Unauthorized action", "danger")
        return redirect(url_for("main.dashboard"))

    task.complete = not task.complete
    db.session.commit()

    return redirect(url_for("main.dashboard"))


# ---------------- DELETE TASK ----------------
@task_bp.route("/task/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash("Unauthorized action", "danger")
        return redirect(url_for("main.dashboard"))

    db.session.delete(task)
    db.session.commit()

    flash("Task deleted", "info")
    return redirect(url_for("main.dashboard"))
