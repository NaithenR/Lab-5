#Naithen Ramirez, cris padilla Lab 5, Group 12

from task import Task

def main_menu():
    pass

def read_file():
    task_list = []
    
    with open("tasklist.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            task_objects = line.strip().split(",")
            if len(task_objects) == 3:
                desc, date, time, = task_objects                
                task = Task(desc, date, time)
                task_list.append(task)
    return task_list

def write_file(tasklist):
    with open("tasklist.txt","w") as file:
        for task in tasklist:
                file.write(f"{repr(task)}\n")


def get_date():
    pass

def get_time():
    pass

def main():
  
    tasks = [
        Task("Complete project", "09/30/2024", "10:00"),
        Task("Attend meeting", "09/28/2024", "14:00")
]
    write_file(tasks)
    loaded_tasks = read_file()
    for task in loaded_tasks:
        print(task)

main()