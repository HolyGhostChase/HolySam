# To-Do List App

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a new task"""
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    """View all tasks"""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    """Delete a task"""
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Deleted task: {deleted}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Load existing tasks
tasks = load_tasks()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")