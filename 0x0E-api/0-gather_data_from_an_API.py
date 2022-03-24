#!/usr/bin/python3
""""Task 0"""
from sys import argv
import json
from urllib import request


if __name__ == "__main__":

    req = request.urlopen('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))
    user = json.loads(req.read())

    req = request.urlopen('https://jsonplaceholder.typicode.com/todos')
    todo_all = json.loads(req.read())

    req.close()

    todo = []
    success = 0

    for item in todo_all:
        if str(item.get("userId")) == argv[1]:
            todo.append(item)
            if item.get("completed") is True:
                success += 1

    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), success, len(todo)))

    for item in todo:
        if item.get("completed") is True:
            print("\t {}".format(item.get("title")))
