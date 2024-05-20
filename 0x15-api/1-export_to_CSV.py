#!/usr/bin/python3

"""
This module uses this REST API https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her TODO list progress.
and export it to csv file
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_request = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1]))

    user = user_request.json()
    user_name = user["username"]

    res = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                       .format(argv[1]))

    tasks = res.json()

    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w', newline="\n") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        user_tasks = [[argv[1], user_name, task['completed'], task['title']]
                      for task in tasks]

        csv_writer.writerows(user_tasks)
