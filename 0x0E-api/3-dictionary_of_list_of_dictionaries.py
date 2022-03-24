#!/usr/bin/python3
""""Task 3"""
import json
from sys import argv
from urllib import request

if __name__ == "__main__":

    req = request.urlopen('https://jsonplaceholder.typicode.com/users')
    user = json.loads(req.read())

    req = request.urlopen('https://jsonplaceholder.typicode.com/todos')
    todo_all = json.loads(req.read())

    req.close()

    json_dict = {}

    for i in range(len(user)):
        todo = []
        for item in todo_all:
            if i + 1 == item.get("userId"):
                tmp_dict = {}
                tmp_dict["username"] = user[i].get("username")
                tmp_dict["task"] = item.get("title")
                tmp_dict["completed"] = item.get("completed")
                todo.append(tmp_dict)
        json_dict[str(i + 1)] = todo

    with open("todo_all_employees.json", 'w') as f:
        f.write(str(json_dict))
