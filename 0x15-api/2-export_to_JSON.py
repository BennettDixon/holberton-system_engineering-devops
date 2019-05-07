#!/usr/bin/python3
"""script for parsing web data from an api
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    base_url = 'https://jsonplaceholder.typicode.com/'
    try:
        employee_id = sys.argv[1]
    except:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        exit(1)

    # grab the info about the user
    url = base_url + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    user_name = user[0].get('username')

    # grab the info about the user's tasks
    url = base_url + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    user_id_key = str(employee_id)
    builder = {user_id_key: []}
    for obj in objs:
            json_data = {
                "task": obj.get('title'),
                "completed": obj.get('completed'),
                "username": user_name
            }
            builder[user_id_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(employee_id), 'w') as myFile:
        myFile.write(json_encoded_data)
