#!/usr/bin/python3
"""script for parsing web data from an api
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    base_url = 'https://jsonplaceholder.typicode.com/'

    # grab info about all users
    url = base_url + 'users'
    response = requests.get(url)
    users = json.loads(response.text)

    # grab the info about the users' tasks
    builder = {}
    for user in users:
        employee_id = user.get('id')
        user_id_key = str(employee_id)
        username = user.get('username')
        builder[user_id_key] = []
        url = base_url + 'todos?userId={}'.format(employee_id)

        response = requests.get(url)
        objs = json.loads(response.text)
        for obj in objs:
                json_data = {
                    "task": obj.get('title'),
                    "completed": obj.get('completed'),
                    "username": username
                }
                builder[user_id_key].append(json_data)

    # write the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w') as myFile:
        myFile.write(json_encoded_data)
