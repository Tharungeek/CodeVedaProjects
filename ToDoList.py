import json
import os
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task_name}")

# View tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['task']}")
    else:
        print("⚠️ Invalid task number.")

# Mark task as completed
def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Marked as done: {tasks[task_number - 1]['task']}")
    else:
        print("⚠️ Invalid task number.")

# Command-line menu
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task_name = input("Enter task: ")
            add_task(task_name)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_done(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
