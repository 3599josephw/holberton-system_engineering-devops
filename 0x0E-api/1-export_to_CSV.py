#!/usr/bin/python3
"""Task 1"""
import json
from sys import argv
from urllib import request

if __name__ == "__main__":

    req = request.urlopen('https://jsonplaceholder.typicode.com/users/{}'.
                          format(argv[1]))
    user = json.loads(req.read())

    req = request.urlopen('https://jsonplaceholder.typicode.com/todos')
    todo_all = json.loads(req.read())

    req.close()

    todo = []
    filename = argv[1] + '.csv'

    for item in todo_all:
        if str(item.get("userId")) == argv[1]:
            todo.append(item)

    with open(filename, 'w') as f:
        for item in todo:
            f.write('"%s","%s","%s","%s"\n' %
                    (item.get("userId"),
                    user.get("username"),
                    item.get("completed"),
                    item.get("title")))
