class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def delete_task(self, task_number):
        """Delete a task from the list by its number."""
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        """Clear all tasks."""
        self.tasks.clear()
        print("All tasks cleared.")

def show_menu():
    """Display the menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    return input("Choose an option: ")

def main():
    todo_list = TodoList()

    while True:
        choice = show_menu()

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)

        elif choice == '4':
            todo_list.clear_tasks()

        elif choice == '5':
            print("Exiting the To-Do List App.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
