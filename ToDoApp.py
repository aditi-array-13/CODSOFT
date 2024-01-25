# CodSoft
# Task 1
# To-Do-App

import tkinter as tk
from datetime import datetime


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Widgets
        self.label = tk.Label(master, text="To-Do List", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.show_button = tk.Button(master, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack(pady=5)

    def add_task(self):
        description = self.task_entry.get()
        if description:
            task = {'description': description, 'created_at': str(datetime.now()), 'completed': False}
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)  # Clear the entry widget
            self.show_tasks()

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for index, task in enumerate(self.tasks, start=1):
            status = 'Done' if task['completed'] else 'Pending'
            self.task_listbox.insert(tk.END, f"{index}. {task['description']} - {status}")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.tasks[selected_index]['completed'] = True
            self.show_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
