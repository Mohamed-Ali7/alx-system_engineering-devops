#!/usr/bin/python3

"""This module contains recurse() functions"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "limit": 25}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        return None
    hot_list.extend([post["data"]["title"] for post in children])
    after = data.get("after", None)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
