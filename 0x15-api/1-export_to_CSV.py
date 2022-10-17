#!/usr/bin/python3
""" for a given employee ID, returns
    information about his/her TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    tasks_count = 0

    r_td = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                        emp_id)
    r_usr = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         emp_id)

    for tasks in r_td.json():
        f = open(str(r_usr.json().get("id")) + ".csv", "a")
        f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                r_usr.json().get("id"), r_usr.json().get("username"),
                tasks.get("completed"), tasks.get("title")))
        f.close()
