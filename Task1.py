# DecodeLabs - Project 1
# To-Do List

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() != "":
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    # View all tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=>
                print(f"{i}. {task}")

    # Exit
    elif choice == "3":
        print("Thank you for using the To-Do List!>
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter 1, 2, >
