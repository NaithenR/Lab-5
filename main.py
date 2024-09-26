#Naithen Ramirez, cris padilla Lab 5, Group 12

from task import Task

def main_menu():
    print("1. Display current task")
    print("2. Mark current task complete")
    print("3. Postpone current task")
    print("4. Add new task")
    print("5. Save and quit")

    choice = int(input("Enter choice:"))

    if choice in range(1,6):
         return choice
    else:
         print("Invalid choice")

def read_file():
    task_list = []
    
    with open("tasklist.txt","r") as file:
        lines = file.readlines()
        for line in lines:
                desc, date, time = line.strip().split(",")                
                task = Task(desc, date, time)
                task_list.append(task)
    return task_list

def write_file(tasklist):
    with open("tasklist.txt","w") as file:
        for task in tasklist:
                file.write(f"{repr(task)}\n")


def get_date():
    month = int(input("Enter month:"))
    day = int(input("Enter Day"))
    year = int(input("Enter Year"))
    if 1<= month <= 12 and 1 <= day<= 31 and 2000 <= year <=2100:
         return f"{month:02d}/{day:02d}/{year}"
    else:
        print("Invalid input.")

def get_time():
    hour = int(input("Enter Hour:"))
    minute= int(input("Enter minute:"))
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        return f"{hour:02d}:{minute:02d}"
    else:
        print("Invalid input.")


def main():
    pass

