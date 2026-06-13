from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Error: Title cannot be empty.")
    return True
    
def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Error: Description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Error: Description cannot be more than 500 characters.")
    return True
    
def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Error: Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Error: Due date must be in YYYY-MM-DD format.")