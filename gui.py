import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import save_to_database
from database import complete_task_in_database
from database import get_last_inserted_id
from database import delete_task_from_database
import webbrowser

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

        self.instagram_button = tk.Button(self.frame, text="", command=self.open_instagram, bg="#000000", fg="#000000", borderwidth=0, cursor="hand2")
        self.instagram_button.place(relx=0, rely=1, anchor='sw', width=20, height=20)


    def add_task(self):
        description = self.task_entry.get()
        due_date_str = self.date_entry.get()

        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M')
        except ValueError:
            messagebox.showerror("Invalid date", "Please enter a valid date in YYYY-MM-DD HH:MM format")
            return

        if description and due_date_str:
            success = save_to_database("valeriamirza5@gmail.com", description, due_date)
            if success:
                task_id = get_last_inserted_id()
                task = Task(task_id, description, due_date)
                self.tasks.append(task)
                self.update_task_list()
                self.task_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)

            else:
                messagebox.showerror("Database Error", "Failed to save task to the database.")
        else:
            messagebox.showerror("Missing information", "Please enter both task description and due date")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task.completed = True
            complete_task_in_database(task.id)
            self.update_task_list()
        else:
            messagebox.showerror("No selection", "Please select a task to complete")


    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task_id = task.id
            del self.tasks[selected_task_index[0]]
            self.update_task_list()
            delete_task_from_database(task_id)
        else:
            messagebox.showerror("No selection", "Please select a task to delete")


    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))


    def open_instagram(self):
        webbrowser.open("https://www.instagram.com/sigmo.ai/?igshid=YmMyMTA2M2Y%3D")

