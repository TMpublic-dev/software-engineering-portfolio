"""
Main entry point for TaskFlow Productivity Manager.

Run with:
    py run.py

The application uses SQLite and automatically creates its own database
the first time it is launched, so no external dataset is required.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
