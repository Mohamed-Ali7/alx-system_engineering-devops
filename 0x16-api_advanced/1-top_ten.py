#!/usr/bin/python3

"""This module contains top_ten() functions"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={"limit": 10})

    if response.status_code == 200:
        posts_data = response.json()['data']['children']
        for post in posts_data[:10]:
            print(post['data']['title'])
    else:
        print("None")
