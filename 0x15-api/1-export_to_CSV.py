#!/usr/bin/python3
""""
Script that, using this REST API,
for a given employee ID, returns information
about his/her TODOs list progress.
"""
import csv
from requests import get
import sys


def user_data_from_api(userId):
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    username = user.json().get('username')
    response = get('https://jsonplaceholder.typicode.com/users/{}/todos'
                   .format(userId))
    data = response.json()

    with open("{}.csv".format(userId), mode="w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in data:
            ls = [userId, username, task.get('completed'), task.get('title')]
            csv_writer.writerow(ls)


if __name__ == "__main__":
    user_data_from_api(sys.argv[1])
