import json
from datetime import datetime
import os
from prettytable import PrettyTable

class Tasky:
    """A simple task manager class that saves tasks to a JSON file."""
    def __init__(self, json_file = "tasks.json"):
        self.json_file = json_file
        self.table_header = ("Id", "Description", "Status", "Last Modified")

        if not os.path.isfile(self.json_file):
            with open(self.json_file, "w") as file:
                file.write("[]")

        with open(json_file, "r") as file:
            self.tasks_list = json.load(file)

        if self.tasks_list:
            self.next_id = max(task['id'] for task in self.tasks_list) + 1
        else:
            self.next_id = 1
        
    def update_task(self):
        """Writes the current tasks list back to the JSON file."""
        with open(self.json_file, "w") as file:
            json.dump(self.tasks_list, file, indent=2)
        
    def add_task(self, taskDesc, taskStat = "pending"):
        """Adds a new task with a unique ID and current timestamp."""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_task = {
            'id': self.next_id, # Use the determined next ID
            'taskDesc': taskDesc, 
            'taskStat': taskStat, 
            'lastMod': current_time
        }
        self.tasks_list.append(new_task)
        self.next_id += 1
        self.update_task()

    def remove_task(self, task_id):
        """Removes a task by its ID."""
        original_length = len(self.tasks_list)
        self.tasks_list = [task for task in self.tasks_list if task['id'] != task_id]
        
        if len(self.tasks_list) < original_length:
            self.update_task()
            return True
        return False

    def list_task(self, filter=None):
        """Prints the list of tasks in a readable table format."""
        table = PrettyTable()
        table.field_names = self.table_header

        tasks_to_list = self.tasks_list
        if filter in ('pending', 'completed'):
            tasks_to_list = [t for t in self.tasks_list if t['taskStat'] == filter]

        if not tasks_to_list:
            print("No tasks found.")
            return

        for task in tasks_to_list:
            table.add_row([
                task['id'], 
                task['taskDesc'], 
                task['taskStat'].capitalize(), 
                task['lastMod']
            ])
        
        table.align["Id"] = "r"
        table.align["Description"] = "l"
        table.align["Status"] = "c"
        table.align["Last Modified"] = "l"

        print(table)
