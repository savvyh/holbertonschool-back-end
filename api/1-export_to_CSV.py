#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
import sys


def get_todo_progress(USER_ID):
    """script TO DO list"""
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USER_ID = user_data['id']
    USERNAME = user_data['name']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f"{USER_ID}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        field = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=field,
                                quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': USER_ID,
                'USERNAME': USERNAME,
                'TASK_COMPLETED_STATUS': 'True'
                if task['completed'] else 'False',
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
