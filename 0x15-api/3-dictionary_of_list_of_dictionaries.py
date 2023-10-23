#!/usr/bin/python3
""""
Script that, using this REST API,
for a given employee ID, returns information
about his/her TODOs list progress.
"""
import json
from requests import get
import sys


def user_data_from_api():

    with open("todo_all_employees.json", mode="w") as f:
        task_data = {}
        
        for i in range(1, 11):
            user = get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(i))
            username = user.json().get('username')
            resp = get('https://jsonplaceholder.typicode.com/users/{}/todos'
                       .format(i))
            data = resp.json()
            ls = []
            for task in data:
                row = {}
                row["username"] = username
                row["task"] = task.get('title')
                row["completed"] = task.get('completed')
                ls.append(row)
            task_data[i] = ls
        json.dump(task_data, f)


if __name__ == "__main__":
    user_data_from_api()
