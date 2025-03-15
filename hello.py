# Simple To-Do List App
tasks = []  # Empty list to store tasks

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    
    elif choice == "2":
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")


