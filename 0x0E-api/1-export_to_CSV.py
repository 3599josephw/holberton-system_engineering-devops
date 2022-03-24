#!/usr/bin/python3
"""Task 1"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()

    todoall = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo = []
    filename = argv[1] + '.csv'

    for item in todoall:
        if str(item.get("userId")) == argv[1]:
            todo.append(item)

    with open(filename, 'w') as f:
        for item in todo:
            f.write('"%s","%s","%s","%s"\n' % (item.get("userId"),
                                               user.get("username"),
                                               item.get("completed"),
                                               item.get("title")))
