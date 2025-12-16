from logic import Tasky
import sys

# Initialize the Tasky manager
tasky = Tasky()

def display_help():
    """Displays the available commands."""
    print("\n--- Tasky Commands ---")
    print("add        - Add a new task.")
    print("list       - List all tasks.")
    print("list pending - List only pending tasks.")
    print("list completed - List only completed tasks.")
    print("rem <ID>   - Remove a task by its ID.")
    print("exit       - Close the application.")
    print("help       - Display this help message.")
    print("----------------------\n")

def run_app():
    """Main application loop."""
    display_help()
    
    while True:
        try:
            user_input = input("Enter Command >>> ").strip().lower()
            
            if user_input == "exit":
                print("Tasky closed. Goodbye!")
                break

            elif user_input == "help":
                display_help()

            elif user_input == "add":
                desc = input("Task description >>> ").strip()
                if desc:
                    tasky.add_task(desc)
                    print(f"Task '{desc}' added successfully!")
                else:
                    print("Error: Task description cannot be empty.")

            elif user_input.startswith("list"):
                parts = user_input.split()
                if len(parts) == 1:
                    tasky.list_task() # List all
                elif len(parts) == 2 and parts[1] in ('pending', 'completed'):
                    tasky.list_task(filter=parts[1]) # List filtered
                else:
                    print("Invalid list command. Use 'list', 'list pending', or 'list completed'.")

            elif user_input.startswith("rem"):
                try:
                    parts = user_input.split()
                    if len(parts) < 2:
                        print("Error: Please specify the ID of the task to remove (e.g., rem 5).")
                        continue
                        
                    task_id = int(parts[1])
                    if tasky.remove_task(task_id):
                        print(f"Task with ID {task_id} removed successfully.")
                    else:
                        print(f"Error: Task with ID {task_id} not found.")
                except ValueError:
                    print("Error: Task ID must be a number.")
                    
            else:
                print(f"Unknown command: '{user_input}'. Type 'help' for a list of commands.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_app()
