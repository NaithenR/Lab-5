
class Task:    
    """Represents task description, date and time
    Attributes:
        description (string): string description of task
        date (string): due date of task. MM/DD/YYYY
        time (string): time the task is due. HH:MM
    """
    def __init__(self, desc, date, time): 
        """
        Initializes a new Task instance.
        
        Args:
            desc (str): Description of the task.
            date (str): Due date of the task in MM/DD/YYYY format.
            time (str): Time the task is due in HH:MM format.
        """
        self.desc = desc
        self.date = date
        self.time = time
    
    def get_description(self):
        """
        Returns the description of the task.
        
        Returns:
            str: The description of the task.
        """
        return self.desc
    
    def __str__(self):
        """
        Returns a string representation of the task for debugging.
        
        Returns:
            str: A string in the format 'description,date,time'.
        """
        return f"{self.desc} Due: {self.date} at {self.time}"

    def __repr__(self):
        """
        Returns a string representation of the task for debugging.
        
        Returns:
            str: A string in the format 'description,date,time'.
        """
        return f"{self.desc},{self.date},{self.time}"

    def __lt__(self, other):
        """
        Compares this task with another task based on their due dates and times.
        
        Args:
            other (Task): The other task to compare with.
        
        Returns:
            bool: True if this task is due before the other task, False otherwise.
        """
        self_month, self_day, self_year = map(int, self.date.split('/'))
        self_hour, self_minute = map(int, self.time.split(':'))
        other_month, other_day, other_year = map(int, other.date.split('/'))
        other_hour, other_minute = map(int, other.time.split(':'))

        if self_year != other_year:
            return self_year < other_year
        if self_month != other_month:
            return self_month < other_month
        if self_day != other_day:
            return self_day < other_day
        if self_hour != other_hour:
            return self_hour < other_hour
        if self_minute != other_minute:
            return self_minute < other_minute
        
        return self.desc < other.desc