#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    '''Returns the number of subscribers for a given subreddit.'''
    if subreddit is None or type(subreddit) is not str:
        return None
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after, 'count': count, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for child in data.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after, count)
