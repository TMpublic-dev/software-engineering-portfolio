"""
Task data access functions.

This file keeps SQL/database code away from the Flask route functions.
That makes the project easier to maintain, test and explain in interviews.
"""

from datetime import datetime
from .database import get_db_connection


VALID_PRIORITIES = ["Low", "Medium", "High", "Urgent"]
VALID_STATUSES = ["To Do", "In Progress", "Completed"]


def get_all_tasks(search="", status="All", priority="All", category="All"):
    """
    Return tasks using optional search and filter values.
    """
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if search:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if status != "All":
        query += " AND status = ?"
        params.append(status)

    if priority != "All":
        query += " AND priority = ?"
        params.append(priority)

    if category != "All":
        query += " AND category = ?"
        params.append(category)

    query += """
        ORDER BY
            CASE status
                WHEN 'In Progress' THEN 1
                WHEN 'To Do' THEN 2
                WHEN 'Completed' THEN 3
                ELSE 4
            END,
            CASE priority
                WHEN 'Urgent' THEN 1
                WHEN 'High' THEN 2
                WHEN 'Medium' THEN 3
                WHEN 'Low' THEN 4
                ELSE 5
            END,
            due_date IS NULL,
            due_date ASC,
            created_at DESC
    """

    conn = get_db_connection()
    tasks = conn.execute(query, params).fetchall()
    conn.close()
    return tasks


def get_task(task_id):
    """Return one task by ID."""
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return task


def create_task(title, description, category, priority, status, due_date):
    """
    Create a new task after basic validation.
    """
    title = title.strip()
    description = description.strip()
    category = category.strip() or "General"

    if not title:
        raise ValueError("Task title is required.")

    if priority not in VALID_PRIORITIES:
        priority = "Medium"

    if status not in VALID_STATUSES:
        status = "To Do"

    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO tasks (title, description, category, priority, status, due_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (title, description, category, priority, status, due_date or None),
    )
    conn.commit()
    conn.close()


def update_task(task_id, title, description, category, priority, status, due_date):
    """
    Update an existing task.
    """
    title = title.strip()
    description = description.strip()
    category = category.strip() or "General"

    if not title:
        raise ValueError("Task title is required.")

    completed_at = None
    if status == "Completed":
        completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    conn.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, category = ?, priority = ?,
            status = ?, due_date = ?, completed_at = ?
        WHERE id = ?
        """,
        (title, description, category, priority, status, due_date or None, completed_at, task_id),
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    """Delete a task permanently."""
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def quick_update_status(task_id, new_status):
    """
    Quickly update the status of a task from the dashboard.
    """
    completed_at = None
    if new_status == "Completed":
        completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    conn.execute(
        "UPDATE tasks SET status = ?, completed_at = ? WHERE id = ?",
        (new_status, completed_at, task_id),
    )
    conn.commit()
    conn.close()


def get_categories():
    """Return unique task categories for the filter dropdown."""
    conn = get_db_connection()
    categories = conn.execute("SELECT DISTINCT category FROM tasks ORDER BY category ASC").fetchall()
    conn.close()
    return [row["category"] for row in categories]


def get_dashboard_stats():
    """
    Calculate dashboard statistics.
    """
    conn = get_db_connection()

    total_tasks = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()["count"]
    completed_tasks = conn.execute("SELECT COUNT(*) AS count FROM tasks WHERE status = 'Completed'").fetchone()["count"]
    in_progress_tasks = conn.execute("SELECT COUNT(*) AS count FROM tasks WHERE status = 'In Progress'").fetchone()["count"]
    urgent_tasks = conn.execute(
        "SELECT COUNT(*) AS count FROM tasks WHERE priority = 'Urgent' AND status != 'Completed'"
    ).fetchone()["count"]
    overdue_tasks = conn.execute(
        """
        SELECT COUNT(*) AS count
        FROM tasks
        WHERE due_date IS NOT NULL
          AND due_date < DATE('now')
          AND status != 'Completed'
        """
    ).fetchone()["count"]

    conn.close()

    completion_rate = round((completed_tasks / total_tasks) * 100, 1) if total_tasks else 0

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "urgent_tasks": urgent_tasks,
        "overdue_tasks": overdue_tasks,
        "completion_rate": completion_rate,
    }
