class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Task "{deleted_task["task"]}" deleted.')
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f'Task "{self.tasks[task_index - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('Tasks in the to-do list:')
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f'{idx}. {task["task"]} - {status}')


if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
