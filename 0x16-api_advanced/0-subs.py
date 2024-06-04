#!/usr/bin/python3

"""This module contains number_of_subscribers functions"""

import json
import urllib.request


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """

    file_name = "access_token"
    access_token = ''
    with open(file_name, 'r') as file:
        access_token = "bearer {}".format(file.read().strip())

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36",
               "Authorization": access_token}

    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data['data']['subscribers']
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return 0
