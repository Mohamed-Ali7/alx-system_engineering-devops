#!/usr/bin/python3

"""This module contains number_of_subscribers functions"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"}

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    return response.json().get('data').get('subscribers')
