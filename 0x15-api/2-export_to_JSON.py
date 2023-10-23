#!/usr/bin/python3
""""
Script that, using this REST API,
for a given employee ID, returns information
about his/her TODOs list progress.
"""
import json
from requests import get
import sys


def user_data_from_api(userId):
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    username = user.json().get('username')
    response = get('https://jsonplaceholder.typicode.com/users/{}/todos'
                   .format(userId))
    data = response.json()

    with open("{}.json".format(userId), mode="w") as f:
        ls = []
        task_data = {}
        for task in data:
            row = {}
            row["task"] = task.get('title')
            row["completed"] = task.get('completed')
            row["username"] = username
            ls.append(row)
        task_data[userId] = ls
        json.dump(task_data, f)


if __name__ == "__main__":
    user_data_from_api(sys.argv[1])
