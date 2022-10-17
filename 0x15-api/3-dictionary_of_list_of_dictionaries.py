#!/usr/bin/python3
""" for a given employee ID, returns
    information about his/her TODO list progress
"""


import json
import requests

if __name__ == "__main__":
    tasks_count = 0

    r_usr = requests.get('https://jsonplaceholder.typicode.com/users/')

    dictionary = {}
    for user in r_usr.json():
        dictionary.update({str(user.get("id")): []})
        r_t = requests.get('https://jsonplaceholder.typicode.com/todos?' +
                           "userId=" + str(user.get("id")))
        for tasks in r_t.json():
            new_dict = {}
            new_dict.update({"username": str(user.get("username")),
                             "task": tasks.get("title"),
                             "completed": tasks.get("completed")})
            dictionary[str(user.get("id"))].append(new_dict)

    f = open("todo_all_employees.json", "w")
    json.dump(dictionary, f)
    f.close()
