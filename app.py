import sys
from backend import Tracker

task = Tracker("app.json")

command = sys.argv[1]

if command == "add":
    task_name = " ".join(sys.argv[2:])
    task.add_task(task_name)
    print(f"Task '{task_name}' added!!")
elif command == "rem":
    task.remove_task(int(sys.argv[2]))
elif command == "ls":
    task.list_tasks()
else:
    print("Please check your input")
