#!/usr/bin/python3
""""Task 3"""
import json
import requests


if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()

    todoall = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    json_dict = {}

    for i in range(len(user)):
        todo = []
        for item in todoall:
            if i + 1 == item.get("userId"):
                tmp_dict = {}
                tmp_dict["username"] = user[i].get("username")
                tmp_dict["task"] = item.get("title")
                tmp_dict["completed"] = item.get("completed")
                todo.append(tmp_dict)
        json_dict[i + 1] = todo

    with open("todo_all_employees.json", 'w') as f:
        json.dump(json_dict, f)
