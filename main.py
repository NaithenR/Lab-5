#Naithen Ramirez, cris padilla Lab 5, Group 12

from task import Task

def main_menu():
    print("-Tasklist-")
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
        print("Invalid date.")

def get_time():
    hour = int(input("Enter Hour:"))
    minute= int(input("Enter minute:"))
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        return f"{hour:02d}:{minute:02d}"
    else:
        print("Invalid time.")


def main():
    tasklist = read_file
    while True:
        print(f"You have {len(tasklist)} tasks.")
        choice = main_menu()

        if choice == 1:
            if tasklist:
                print(f"Current task is: {tasklist[0]}")
            else:
                print("All task are complete.")
        
        elif choice == 2:
             if tasklist:
                print(f"Marking current class as complete: {tasklist[0]}")
                tasklist.pop(0)
                if tasklist:
                    print(f"New current task is: {tasklist[0]}")
                else:
                    print("All task are complete")
        
        elif choice == 3:
            if tasklist:
                current_task = tasklist[0]
                print(f"Postponing task: {current_task}")
                print("Enter new date:")
                new_date = get_date()
                print("Enter new time:")
                new_time = get_time()
                updated_task = Task(current_task.desc, new_date, new_time)
                tasklist.pop(0)
                tasklist.append(updated_task)
                #Call sort