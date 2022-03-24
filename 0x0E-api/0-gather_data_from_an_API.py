#!/usr/bin/python3
""""Task 0"""
import json
import requests
from sys import argv



if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1])).json()

    todo_all = requests.get('https://jsonplaceholder.typicode.com/todos').json()

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
