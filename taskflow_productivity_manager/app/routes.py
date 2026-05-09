"""
Web routes for TaskFlow Productivity Manager.

Routes receive user input, call the model layer and render templates.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import (
    get_all_tasks,
    get_task,
    create_task,
    update_task,
    delete_task,
    quick_update_status,
    get_categories,
    get_dashboard_stats,
    VALID_PRIORITIES,
    VALID_STATUSES,
)


taskflow_bp = Blueprint("taskflow", __name__)


@taskflow_bp.route("/")
def index():
    """Main dashboard showing tasks, filters and summary statistics."""
    search = request.args.get("search", "")
    status = request.args.get("status", "All")
    priority = request.args.get("priority", "All")
    category = request.args.get("category", "All")

    tasks = get_all_tasks(search=search, status=status, priority=priority, category=category)
    stats = get_dashboard_stats()
    categories = ["All"] + get_categories()

    return render_template(
        "index.html",
        tasks=tasks,
        stats=stats,
        search=search,
        selected_status=status,
        selected_priority=priority,
        selected_category=category,
        statuses=["All"] + VALID_STATUSES,
        priorities=["All"] + VALID_PRIORITIES,
        categories=categories,
    )


@taskflow_bp.route("/tasks/new", methods=["GET", "POST"])
def new_task():
    """Create a new task."""
    if request.method == "POST":
        try:
            create_task(
                title=request.form.get("title", ""),
                description=request.form.get("description", ""),
                category=request.form.get("category", "General"),
                priority=request.form.get("priority", "Medium"),
                status=request.form.get("status", "To Do"),
                due_date=request.form.get("due_date", ""),
            )
            flash("Task created successfully.", "success")
            return redirect(url_for("taskflow.index"))
        except ValueError as error:
            flash(str(error), "error")

    return render_template("task_form.html", page_title="Create Task", task=None, priorities=VALID_PRIORITIES, statuses=VALID_STATUSES)


@taskflow_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    """Edit an existing task."""
    task = get_task(task_id)

    if task is None:
        flash("Task not found.", "error")
        return redirect(url_for("taskflow.index"))

    if request.method == "POST":
        try:
            update_task(
                task_id=task_id,
                title=request.form.get("title", ""),
                description=request.form.get("description", ""),
                category=request.form.get("category", "General"),
                priority=request.form.get("priority", "Medium"),
                status=request.form.get("status", "To Do"),
                due_date=request.form.get("due_date", ""),
            )
            flash("Task updated successfully.", "success")
            return redirect(url_for("taskflow.index"))
        except ValueError as error:
            flash(str(error), "error")

    return render_template("task_form.html", page_title="Edit Task", task=task, priorities=VALID_PRIORITIES, statuses=VALID_STATUSES)


@taskflow_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def remove_task(task_id):
    """Delete a task."""
    delete_task(task_id)
    flash("Task deleted.", "success")
    return redirect(url_for("taskflow.index"))


@taskflow_bp.route("/tasks/<int:task_id>/status/<new_status>", methods=["POST"])
def change_status(task_id, new_status):
    """Quickly change a task status from the dashboard."""
    if new_status not in VALID_STATUSES:
        flash("Invalid task status.", "error")
    else:
        quick_update_status(task_id, new_status)
        flash("Task status updated.", "success")

    return redirect(url_for("taskflow.index"))
