#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = (requests.get(url + "/users/{}".format(argv[1])).json().get("name"))
    todos = requests.get(url + "/user/{}/todos".format(argv[1])).json()

    done_titles = []
    done_number = 0
    for todo in todos:
        if todo.get("completed"):
            done_number += 1
            done_titles.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_number, len(todos)))
    for title in done_titles:
        print("\t {}".format(title))
