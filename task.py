
class Task:    
    """Represents task description, date and time
    Attributes:
        description (string): string description of task
        date (string): due date of task. MM/DD/YYYY
        time (string): time the task is due. HH:MM
    """
    def __init__(self, desc, date, time): 
        self.desc = desc
        self.date = date
        self.time = time
    
    def get_description(self):
        return self.desc
    
    def __str__(self):
        return f"{self.desc} Due: {self.date} at {self.time}"

    def __repr__(self):
        return f"{self.desc},{self.date},{self.time}"

    def __lt__(self, other):
        pass