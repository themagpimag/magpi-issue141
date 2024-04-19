# Simple To-Do Program in Python

# Displays the menu
# Returns the user's choice
def display_menu():
    print("\nTo-Do List Program")
    print("1. View To-Do List")
    print("2. Add Task to List")
    print("3. Delete Task from List")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice

# Displays the tasks in the list
def view_tasks(task_list):
    if not task_list: # if the list is empty
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}") # print the task number and the task

# Adds a task to the list
def add_task(task_list):
    task = input("Enter a task to add: ")
    task_list.append(task)
    print(f"'{task}' has been added to the list.")

# Deletes a task from the list
def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num-1)
            print(f"'{removed_task}' has been removed from the list.")
        else:
            print("Invalid task number.")

# Main function
def main():
    task_list = []
    
    while True: # run the program until the user chooses to exit
        user_choice = display_menu() # display the menu and get the user's choice
        
        # process the user's choice
        if user_choice == "1":
            view_tasks(task_list) # pass the task list to the view_tasks function
        elif user_choice == "2":
            add_task(task_list) # pass the task list to the add_task function
        elif user_choice == "3":
            delete_task(task_list) # pass the task list to the delete_task function
        elif user_choice == "4":
            print("Exiting program.") 
            break # exit the program
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__": # if the program is run directly
    main() # run the main function
