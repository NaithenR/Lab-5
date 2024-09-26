#Naithen Ramirez, cris padilla Lab 5, Group 12
# Sep 26 , 2024 
# This program is a task list that allows the user to add, display, postpone, and mark tasks as complete.

import check_input
from task import Task

def main_menu(): # This function is used to display the main menu and return the user's choice.
    print("1. Display current task")
    print("2. Mark current task complete")
    print("3. Postpone current task")
    print("4. Add new task")
    print("5. Save and quit")

    choice = check_input.get_int_range("Enter choice: ", 1, 5)

    if choice in range(1,6):
         return choice
    else:
         print("Invalid choice")

def read_file():
    """
    Reads tasks from a file and returns a list of Task objects.
    
    Returns:
        list: A list of Task objects read from the file.
    """
    task_list = []
    
    with open("tasklist.txt","r") as file:
        lines = file.readlines()
        for line in lines:
                desc, date, time = line.strip().split(",")                
                task = Task(desc, date, time)
                task_list.append(task)
    return task_list

def write_file(tasklist):
    """
    Writes a list of Task objects to a file.
    
    Args:
        tasklist (list): A list of Task objects to be written to the file.
    """
    with open('tasklist.txt', 'w') as file:
        for task in tasklist:
            file.write(task.__repr__() + "\n")


def get_date():
    """
    Prompts the user to enter a date and returns it in MM/DD/YYYY format.
    
    Returns:
        str: The date entered by the user in MM/DD/YYYY format.
    """
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter Day: ", 1, 31)
    year = check_input.get_int_range("Enter Year: ", 2000, 2100)
    
    return f"{month:02d}/{day:02d}/{year}"

def get_time():
    """
    Prompts the user to enter a time and returns it in HH:MM format.
    
    Returns:
        str: The time entered by the user in HH:MM format.
    """
    hour = check_input.get_int_range("Enter Hour: ", 0, 23)
    minute= check_input.get_int_range("Enter minute: ", 0 , 59)
    return f"{hour:02d}:{minute:02d}"



def main():
    tasklist = read_file() # List of Task objects
    tasklist.sort() # Sort tasks by due date and time
    while True:
        print("-Tasklist-")
        print(f"You have {len(tasklist)} tasks.")
        choice = main_menu()

        # Display current task
        if choice == 1:
            if tasklist:
                print(f"Current task is: {tasklist[0]}")
            else:
                print("All task are complete.")
        
        # Mark current task as complete
        elif choice == 2:
             if tasklist:
                print(f"Marking current class as complete: {tasklist[0]}")
                tasklist.pop(0)
                if tasklist:
                    print(f"New current task is: {tasklist[0]}")
                else:
                    print("All task are complete")
        
        # Postpone current task
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
                tasklist.sort()
        
        # Add new task
        elif choice == 4: 
            print("Enter new task description:")
            new_desc = input()
            print("Enter new date:")
            new_date = get_date()
            print("Enter new time:")
            new_time = get_time()
            new_task = Task(new_desc, new_date, new_time)
            tasklist.append(new_task)
            tasklist.sort()
        
        # Save and quit
        elif choice == 5: 
            write_file(tasklist)
            print("Saving and exiting.")
            break
            
            
            
if __name__ == "__main__":
    main()
        
        
    