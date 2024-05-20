#!/usr/bin/python3

"""
This module uses this REST API https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_request = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1]))

    user = user_request.json()
    user_name = user["name"]

    res = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                       .format(argv[1]))

    tasks = res.json()
    total_number_of_tasks = len(tasks)
    number_of_done_tasks = 0
    completed_tasks = []

    for task in tasks:
        if task['completed']:
            number_of_done_tasks += 1
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, number_of_done_tasks, total_number_of_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
