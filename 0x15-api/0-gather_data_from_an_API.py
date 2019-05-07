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
    name = user[0].get('name')

    # grab the info about the user's tasks
    url = base_url + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    completed = 0
    completed_tasks = []
    for obj in objs:
        if obj.get('completed'):
            completed_tasks.append(obj)
            completed += 1

    # print the output about user's task completion
    print("{} is done with tasks({}/{}):".format(name, completed, len(objs)))
    # print the output title of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
