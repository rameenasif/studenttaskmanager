"""Task logic for the Student Task Manager."""
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks(path=TASKS_FILE):
    """Load tasks from a JSON file (empty list if the file does not exist)."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=TASKS_FILE):
    """Save the task list to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    """Add a new task and return it."""
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": new_id, "title": title, "done": False}
    tasks.append(task)
    return task


def show_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")



def complete_task(tasks, task_id):
    """Mark a task as completed. Return True if it was found."""
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False