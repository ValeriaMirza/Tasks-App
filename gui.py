import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Task:
    def __init__(self, id, description, due_date):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.completed = False


    def __str__(self):
        return f"{self.description} (Due: {self.due_date.strftime('%Y-%m-%d %H:%M')}) - {'Completed' if self.completed else 'Pending'}"

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tasks App")
        self.root.geometry("550x450")
        self.root.configure(bg="#000000")

        self.tasks = []

        self.frame = tk.Frame(root, bg="#000000")
        self.frame.pack(pady=10)

        self.task_label = tk.Label(self.frame, text="Task Description", bg="black", fg="white")
        self.task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.task_entry = tk.Entry(self.frame, width=30,bg="#f0f0f0")
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)

        self.date_label = tk.Label(self.frame, text="Due Date (YYYY-MM-DD HH:MM)", bg="black", fg="white")
        self.date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.date_entry = tk.Entry(self.frame, width=30,bg="#f0f0f0")
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="#191970",fg="white")
        self.add_button.grid(row=2, column=1, pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10,bg="#f0f0f0")
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(self.frame, text="Complete Task", command=self.complete_task, bg="green",fg="white")
        self.complete_button.grid(row=4, column=0, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task, bg="red",fg="white")
        self.delete_button.grid(row=4, column=1, pady=5)

    def add_task(self):
        pass
    def complete_task(self):
        pass
    def delete_task(self):
        pass
    def update_task_list(self):
        pass
    def send_email_gui(task):
        pass


root = tk.Tk()
app = TaskApp(root)
root.mainloop()