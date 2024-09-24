#attributes
class Task:
    """Represents task description, date and time
    Attributes:
        description (string): string description of task
        date (string): due date of task. MM/DD/YYYY
        time (string): time the task is due. HH/MM
    """
    def __innit__(self,desc, date, time):
        self.desc = desc
        self.date = date
        self.time = time
    
    def get_description(self):
        pass
    
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __lt__ (self, other):
        pass