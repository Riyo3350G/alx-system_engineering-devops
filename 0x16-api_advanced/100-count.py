#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """parses the title of all hot articles, and prints a sorted count"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            count_words(subreddit, word_list, after, word_dict)
        data = results.json().get("data").get("children")
        for child in data:
            title = child.get("data").get("title")
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        if len(word_dict) == 0:
            return
        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key.lower(), value))
    else:
        return
