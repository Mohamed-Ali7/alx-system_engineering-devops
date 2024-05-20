#!/usr/bin/python3

"""
This module uses this REST API https://jsonplaceholder.typicode.com/
to records all tasks from all employees and dump it to json file
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    users_request = requests.get("https://jsonplaceholder.typicode.com/users")
    tasks_request = requests.get("https://jsonplaceholder.typicode.com/todos")

    users = users_request.json()
    tasks = tasks_request.json()

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:

        employees_tasks = {}
        for user in users:
            user_name = user['username']
            user_id = user['id']

            user_tasks = [
                {
                    "username": user_name,
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in tasks if task['userId'] == user_id
                ]
            employees_tasks[user_id] = user_tasks

        json.dump(employees_tasks, file)
