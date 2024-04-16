#!/usr/bin/python3
"""
Python script to export data in the json format.
"""

import requests
import sys
import json


def export_json(USER_ID):
    """export data in the json format"""
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    todos_url = f"https://jsonplaceholder.typicode.com/\
todos?userId={USER_ID}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data['username']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data in JSON format
    tasks = []
    for task in todos_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": USERNAME
        }
        tasks.append(task_data)

    json_data = {"USER_ID": tasks}

    # Write JSON data to file
    json_filename = f"{USER_ID}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    export_json(USER_ID)
