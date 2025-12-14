from prettytable import PrettyTable
import json
import os

json_file = "tasks.json"

if not os.path.isfile(json_file):
    open(json_file, "w").close()
