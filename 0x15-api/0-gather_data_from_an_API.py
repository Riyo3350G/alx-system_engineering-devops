#!/usr/bin/python3
""""
script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    name = user.json().get('name')
    response = get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()

    total_task = 0
    completed_task = 0
    for task in data:
        if task.get('userId') == int(argv[1]):
            total_task += 1
            if task.get('completed') is True:
                completed_task += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_task, total_task))
    for task in data:
        if task.get('userId') == int(argv[1]):
            if task.get('completed') is True:
                print("\t {}".format(task.get('title')))
