#!/usr/bin/env python3

import sys # Import the sys module to access command-line arguments
import os # Import the os module to check if a file exists

# Define the path to the file
home_dir = os.path.expanduser('~')  # Gets the user's home directory
todo_file = os.path.join(home_dir, 'todo_list.txt')  # Builds the full path

def load_tasks():
    # Load tasks from the file
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Remove newline characters
    else:
        tasks = [] # Return an empty list if the file does not exist
    return tasks

def save_tasks(tasks):
    #Save tasks to the file
    with open(todo_file, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    # Add a new task
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def view_tasks():
    # Display all tasks
    tasks = load_tasks()
    if tasks:
        print("ToDo List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your ToDo list is empty!")

def delete_task(task_number):
    # Delete a task by its number
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    # Check if the user has provided a command
    if len(sys.argv) < 2: # The first argument is the script name
        print("Usage: python todo.py [add/view/delete] [task]")
        return

    command = sys.argv[1].lower()
    if command == 'add':
        task = ' '.join(sys.argv[2:])
        add_task(task)
        print("Task added.")
    elif command == 'view':
        view_tasks()
    elif command == 'delete':
        if len(sys.argv) == 3:
            task_number = int(sys.argv[2])
            delete_task(task_number)
        else:
            print("Usage: python todo.py delete [task number]")
    else:
        print("Invalid command. Use add, view, or delete.")

if __name__ == "__main__":
    main()