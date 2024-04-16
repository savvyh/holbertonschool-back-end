#!/usr/bin/python3
"""
Python script to export data in the JSON format.
Records all tasks from all employees
"""


import json
import requests


def export_all_tasks():
    """export data in JSON format"""
    # Endpoint URL for users
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch all users
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Prepare data in JSON format
    all_employees_data = {}
    for user in users_data:
        employee_id = user['id']
        username = user['username']

    # Endpoint URL for user's TODOs
        todos_url = f"https://jsonplaceholder.typicode.com/\
todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Collect tasks for the user
        user_tasks = []
        for task in todos_data:
            task_data = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_data)

        # Add user tasks to the data
        all_employees_data[employee_id] = user_tasks

    # Write JSON data to file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    export_all_tasks()
