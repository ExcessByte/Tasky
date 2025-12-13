class Tracker():
    """The backend for my task tracker app"""
    def __init__(self, json_file):
        self.json_file = json_file
        self.tasks = {}

        try:
            open(self.json_file, "r").close()
        except FileNotFoundError:
            file = open(self.json_file, 'w')
            file.writelines("[]")
            file.close()

        with open(self.json_file, "r") as file:
            dictionaries = file.read().replace("\n", "")
            file.close()
            self.tasks = {}
            dict_list = eval(dictionaries)
            n = 1
            for i in dict_list:
                self.tasks[n] = i
                n+=1

    def update_tasks(self):
        with open(self.json_file, "w") as file:
            file.writelines("[\n")
            for i in list(self.tasks.keys()):
                file.writelines("{\n")
                file.writelines(f'      "taskName" : "{self.tasks[i]["taskName"]}",\n')
                file.writelines(f'      "taskStatus" : "{self.tasks[i]["taskStatus"]}"\n')
                file.writelines("},\n")
            file.writelines("]")
        
    def add_task(self, task_name : str, task_status="pending"):
        try:
            last_id = list(self.tasks)[-1]
        except:
            last_id = 0
        finally:
            self.tasks[last_id + 1] = {'taskName': task_name, 'taskStatus': task_status}
            self.update_tasks()

    def remove_task(self, task_id : int):
        del self.tasks[task_id]
        self.update_tasks()

    def list_tasks(self):
        for i in self.tasks.keys():
            print(f"{i}. {self.tasks[i]["taskName"]} -- {self.tasks[i]["taskStatus"]}")
        self.update_tasks()
