#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Returns the number of subscribers for a given subreddit.'''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    params = {
        'limit': 100,
        'after': after
        }
    if response.status_code == 404:
        return None
    else:
        result = response.json().get('data')
        after = result.get('after')
        counter = result.get('dist')
        for i in range(counter):
            hot_list.append(result.get('children')[i].get('data').get('title'))
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
