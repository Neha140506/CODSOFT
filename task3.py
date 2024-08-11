import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} [{status}]"

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Task(**task) for task in data]
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def add_task(tasks, description):
    tasks.append(Task(description))

def list_tasks(tasks):
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

def mark_task_completed(tasks, task_index):
    tasks[task_index].completed = True

def main():
    tasks = load_tasks('tasks.json')
    
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Save and Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            list_tasks(tasks)
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == '4':
            save_tasks('tasks.json', tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
