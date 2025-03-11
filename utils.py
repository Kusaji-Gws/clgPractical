class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display!")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def delete_task(self, task_number):
        if task_number > 0 and task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number!")

def main():
    todo = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            todo.display_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            todo.add_task(task)
        elif choice == '3':
            todo.display_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
