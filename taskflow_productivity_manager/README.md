# TaskFlow Productivity Manager

## Project Summary

**TaskFlow Productivity Manager** is a functional web application built with **Python**, **Flask** and **SQLite**. It allows users to create, edit, search, filter, update and delete tasks through a clean dashboard interface.

Unlike a simple static project, TaskFlow is fully usable immediately after running the application. It does not require any external CSV files, APIs or manual database setup. The SQLite database is created automatically the first time the app starts.

This project was designed to demonstrate practical backend development, database use, CRUD functionality, form handling, validation, responsive UI design and clean project structure.

---

# Features

## Task Management

- Create new tasks
- Edit existing tasks
- Delete tasks with confirmation
- Add titles, descriptions, categories, priorities and due dates
- Track task status through To Do, In Progress and Completed stages

## Dashboard

- View all tasks in a responsive card layout
- Search by title or description
- Filter by status
- Filter by priority
- Filter by category
- Quickly update task progress from the dashboard

## Productivity Statistics

- Total task count
- Completed task count
- In-progress task count
- Urgent active task count
- Overdue task count
- Completion rate percentage

## Database Functionality

- Uses SQLite for local persistent storage
- Automatically creates the database on first run
- Stores task details safely in a structured table
- Uses parameterised SQL queries to reduce injection risk
- Keeps database logic separate from route logic

## User Experience

- Clean responsive design
- Mobile-friendly layout
- Flash messages for user feedback
- Form validation
- Deletion confirmation using JavaScript
- Clear status and priority labels

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core backend programming |
| Flask | Web framework and routing |
| SQLite | Local database storage |
| HTML | Page structure |
| CSS | Responsive interface styling |
| JavaScript | Delete confirmation behaviour |
| pytest | Basic testing |
| Git/GitHub | Version control and portfolio hosting |

---

# Skills Demonstrated

This project demonstrates practical experience with:

- Full-stack web development
- Backend routing
- Database design
- SQLite CRUD operations
- Form handling
- Input validation
- Search and filtering
- Dashboard statistics
- Responsive UI design
- Modular project structure
- Maintainable commented code
- User-focused feature design

---

# Repository Structure

```text
taskflow_productivity_manager/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── task_form.html
│   │
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── app.js
│
├── tests/
│   └── test_validation.py
│
├── requirements.txt
├── run.py
└── README.md
```

---

# Running the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/taskflow-productivity-manager.git
```

## 2. Open the project folder

```bash
cd taskflow-productivity-manager
```

## 3. Create a virtual environment

### Windows

```bash
py -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the application

```bash
py run.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# How to Use

1. Open the dashboard.
2. Click **New Task**.
3. Enter a task title, description, category, priority, status and due date.
4. Use the dashboard to search and filter tasks.
5. Use the progress buttons to move tasks between To Do, In Progress and Completed.
6. Edit or delete tasks when needed.

---

# Future Development Goals

Planned improvements include:

- User login system
- Multiple user accounts
- Drag-and-drop Kanban board
- Calendar view
- Email reminders
- Recurring tasks
- Project grouping
- REST API endpoints
- Cloud deployment
- Dark mode
- Export tasks to CSV or PDF

---

# Portfolio Value

This project is useful for a software engineering portfolio because it shows the ability to build a complete working application rather than only a visual mock-up. It includes real user interaction, database storage, validation, filtering, dashboard statistics and a maintainable code structure.
