import sys

def show_menu():
    print("\n==================================================")
    print("               CODSOFT TO-DO TRACKER              ")
    print("==================================================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task Status (Mark Completed)")
    print("4. Delete Task")
    print("5. Exit Application")
    print("--------------------------------------------------")

def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is completely empty! 🎉")
        return
    print("\nCURRENT TASKS:")
    for index, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task["completed"] else "⏳ Pending"
        print(f"{index}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("\nEnter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"Success! '{title}' has been added to your list.")
    else:
        print("Error: Task description cannot be blank.")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print(f"Excellent! Task '{tasks[choice - 1]['title']}' marked complete.")
        else:
            print("Error: Invalid task number selection.")
    except ValueError:
        print("Error: Please input a valid numerical digit.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Removed: '{removed['title']}' has been permanently deleted.")
        else:
            print("Error: Invalid task number selection.")
    except ValueError:
        print("Error: Please input a valid numerical digit.")

def main():
    tasks = []
    while True:
        try:
            show_menu()
            choice = input("Select an option (1-5): ").strip()
            if choice == '1':
                view_tasks(tasks)
            elif choice == '2':
                add_task(tasks)
            elif choice == '3':
                update_task(tasks)
            elif choice == '4':
                delete_task(tasks)
            elif choice == '5':
                print("\nExiting To-Do List application. Have a great day!")
                break
            else:
                print("Error: Invalid menu choice. Please select 1, 2, 3, 4, or 5.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()