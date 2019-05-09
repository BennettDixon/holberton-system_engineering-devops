#!/usr/bin/python3
"""script for parsing web data from an api
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(
        subreddit
    )
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    if len(hot_list) == 0:
        # grab info about all users
        url = base_url
    else:
        url = base_url + '?after={}_{}'.format(
            hot_list[-1].get('kind'),
            hot_list[-1].get('data').get('id')
        )
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)
    try:
        # grab the info about the users' tasks
        data = resp.get('data')
        children = data.get('children')
    except:
        return None
    if children is None or data is None or len(children) < 1:
        return hot_list
    hot_list.extend(children)
    return recurse(subreddit, hot_list)
