#!/usr/bin/python3

"""This module contains number_of_subscribers functions"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """

    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}


    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    return response.json().get('data').get('subscribers')
