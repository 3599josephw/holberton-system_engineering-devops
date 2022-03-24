#!/usr/bin/python3
""""Task 2"""
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
    filename = argv[1] + '.json'

    for item in todo_all:
        tmp_dict = {}
        if str(item.get("userId")) == argv[1]:
            tmp_dict["task"] = item.get("title")
            tmp_dict["completed"] = item.get("completed")
            tmp_dict["username"] = user.get("username")
            todo.append(tmp_dict)

    json_dict = {argv[1]: todo}

    with open(filename, 'w') as f:
        f.write(str(json_dict))
