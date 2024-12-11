"""
    To-Do List Project: 
    
"""
# empty list
to_do_list = []

# menu that welcomes users and shows menu items
def menu():
    print("\nWelcome to your To-Do List!")
    print("1. [Add]. Add a task")
    print("2. [View]. View list")
    print("3. [Del]. Delete a task")
    print("4. [Quit]. Quit")

# function to add tasks
def add_task():
    task = input("Enter a task: ")
    to_do_list.append(task)
    print(f"Your task {task} has been added to the list.")
     
# funtion to view tasks
def view_tasks():
    if to_do_list:
        print("Here are your tasks: ")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index} {task}")
    else:
        print("There are no tasks.")
            
# function to delete a task   
def delete_task():
    view_tasks()
    if to_do_list:
        try:
            deleted_task = to_do_list.pop(int(input("Enter the task you want to delete.")))
            print("Deleting task.")
            # deleted_task = tasks.pop(int(task_number)- 1)
            print(f"The task '{deleted_task} was deleted.")
        except Exception as e:
            print(f"Invalid number entry. {e}")
        finally:
            print("Thank you!")
            
# function to explain program
def main():
    while True:
        menu()
        command = input("Please choose 1 [add], 2 [view], 3 [del], 4 [quit]: ").lower()
        
        if command == "add" or command == "1":
            add_task()
        elif command == "view" or command == "2":
            view_tasks()
        elif command == "del" or command == "3":
            delete_task()
        elif command == "quit" or command == "4":
            print("Quitting, we are done here. Have an amazing day!.")
            break        
        else:
            print("This is not a valid command. Please try again.")
main()
