import tkinter as tk
from gui import TaskApp
from database import create_database_and_table_if_not_exists
from scheduler import start_scheduler


def main():

    create_database_and_table_if_not_exists()

    start_scheduler()

    root = tk.Tk()
    TaskApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
