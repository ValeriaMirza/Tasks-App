class Task:
    def __init__(self, id, description, due_date):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.completed = False


    def __str__(self):
        return f"{self.description} (Due: {self.due_date.strftime('%Y-%m-%d %H:%M')}) - {'Completed' if self.completed else 'Pending'}"
