#!/usr/bin/python3
""""Task 2"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()

    todoall = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo = []
    filename = argv[1] + '.json'

    for item in todoall:
        tmp_dict = {}
        if str(item.get("userId")) == argv[1]:
            tmp_dict["task"] = item.get("title")
            tmp_dict["completed"] = item.get("completed")
            tmp_dict["username"] = user.get("username")
            todo.append(tmp_dict)

    json_dict = {user.get("id"): todo}

    with open(filename, 'w') as f:
        json.dump(json_dict, f)
