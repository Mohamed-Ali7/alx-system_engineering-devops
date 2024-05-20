#!/usr/bin/python3

"""
This module uses this REST API https://jsonplaceholder.typicode.com/
to records all tasks from all employees and dump it to json file
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_request = requests.get("{}".format(users_url))

    users = users_request.json()

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:

        employees_tasks = {}
        for user in users:
            user_tasks_request = requests.get("{}/{}/todos/"
                                              .format(users_url, user['id']))
            tasks = user_tasks_request.json()
            employees_tasks[user['id']] = []
            for task in tasks:
                employees_tasks[user['id']].append(
                    {"username": user['username'], "task": task['title'],
                     "completed": task['completed']}
                )
        json.dump(employees_tasks, file)
