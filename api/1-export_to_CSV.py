#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import csv
import requests
import sys


def export_csv(USER_ID):
    """export data in the csv format"""
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data['name']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f"{USER_ID}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            TASK_COMPLETED_STATUS = task
            TASK_TITLE = task
            csv_writer.writerow([USER_ID, USERNAME,
                                 TASK_COMPLETED_STATUS['completed'],
                                 TASK_TITLE['title']])


if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    export_csv(USER_ID)
