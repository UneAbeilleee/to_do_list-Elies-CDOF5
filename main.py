import csv
import tkinter as tk
from tkinter import messagebox, scrolledtext

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                self.tasks = [{'task': row[0], 'completed': row[1] == 'True'} for row in reader]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task['task'], str(task['completed'])])

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')
        self.save_tasks()

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Task "{deleted_task["task"]}" deleted.')
            self.save_tasks()
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print(f'Task "{self.tasks[task_index - 1]["task"]}" marked as completed.')
            self.save_tasks()
        else:
            print("Invalid task index.")

    def get_tasks(self):
        return self.tasks

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.todo_list = ToDoList()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="To-Do List")
        self.label.pack()

        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(self.master, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.show_button = tk.Button(self.master, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        self.text_display = scrolledtext.ScrolledText(self.master, width=40, height=10)
        self.text_display.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = int(tk.simpledialog.askstring("Delete Task", "Enter task index to delete:"))
            self.todo_list.delete_task(task_index)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid task index.")

    def complete_task(self):
        try:
            task_index = int(tk.simpledialog.askstring("Complete Task", "Enter task index to mark as completed:"))
            self.todo_list.complete_task(task_index)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid task index.")

    def show_tasks(self):
        tasks = self.todo_list.get_tasks()
        if not tasks:
            self.text_display.delete(1.0, tk.END)  # Efface le texte actuel dans le widget Text
            self.text_display.insert(tk.END, 'No tasks in the to-do list.')
        else:
            self.text_display.delete(1.0, tk.END)  # Efface le texte actuel dans le widget Text
            self.text_display.insert(tk.END, 'Tasks in the to-do list:\n')
            for idx, task in enumerate(tasks, start=1):
                status = "Completed" if task['completed'] else "Not Completed"
                self.text_display.insert(tk.END, f'{idx}. {task["task"]} - {status}\n')

if __name__ == "__main__":
   root = tk.Tk()
   app = ToDoListGUI(root)
   root.mainloop()
   

