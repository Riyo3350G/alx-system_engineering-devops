#!/usr/bin/python3
"""
    function that queries the Reddit API and prints the titles o
    f the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    '''Returns the number of subscribers for a given subreddit.'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    dict = response.json()
    if response.status_code == 200:
        for i in range(10):
            print(dict.get('data').get('children')[i].get('data').get('title'))
            print()
    else:
        print(None)
