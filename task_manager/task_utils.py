from datetime import datetime
# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Error: Invalid task number.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks!")
    else:
        print("\n--- Pending Tasks ---")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task['title']} | {task['description']} | Due: {task['due_date']}")
        print("---------------------")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        progress = 0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100
        print(f"Progress: {completed}/{len(tasks)} tasks completed ({progress:.1f}%)")
    return progress