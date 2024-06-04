#!/usr/bin/python3

"""This module contains recurse() functions"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/125.0.0.0 Safari/537.36"}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        return None

    titles = ([post["data"]["title"] for post in children])
    word_list = [word.lower() for word in word_list]
    for title in titles:
        title_words = [word.lower() for word in title.split()]
        for word in word_list:
            count = title_words.count(word)
            if word not in word_count:
                word_count[word] = count
            else:
                word_count[word] += count

    after = data.get("after", None)
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        word_count = sorted(word_count.items(),
                            key=lambda item: (-item[1], item[0]))
        for word, count in word_count:
            print("{}: {}".format(word, count))
