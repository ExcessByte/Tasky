import sys
from backend import Tracker

task = Tracker("app.json")

try:
    if len(sys.argv) > 1:
        command = args[1].lower()

        if command == "add":
            try:
                task_name = args[2]
                task.add_task(task_name)
                print(f"Task '{task_name}' added!")
            except IndexError:
                print("Error: The 'add' command requires a task name.")

        elif command == "rem":
            try:
                index_str = args[2]
                index = int(index_str)
                task.remove_task(index)
                print(f"Task at index {index} removed (if it existed).")
            except IndexError:
                print("Error: The 'rem' command requires an index.")
            except ValueError:
                print(f"Error: '{index_str}' is not a valid numerical index.")

        elif command in ("ls", "list"):
            task.list_tasks()

        else:
            print(f"Unrecognized command: {command}")
            print("Available commands: add, rem, ls/list")
    else:
        print("\nWelcome to the interactive shell~~ \nType 'exit' to quit.")
        
        while True:
            command_input = input("\nCommand: ").strip().lower()

            if command_input == "exit":
                break
            
            elif command_input == "add":
                name = input("Enter task name: ").strip()
                if name:
                    task.add_task(name)
                    print(f"Task '{name}' added!")
                else:
                    print("Task name cannot be empty.")

            elif command_input in ("rm", "rem", "remove"):
                index_str = input("Enter the index of the item to remove: ").strip()
                try:
                    index = int(index_str)
                    task.remove_task(index)
                    print(f"Task at index {index} removed")
                except ValueError:
                    print("Invalid input. Please enter a numerical index.")
                except KeyError:
                    print("Index does not exit!")


            elif command_input in ("ls", "list"):
                task.list_tasks()

            else:
                print("Unrecognized command.")
                print("Available commands: add, rem/remove, ls/list, exit")

except KeyboardInterrupt:
    task.update_tasks()
