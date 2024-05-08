#!/usr/bin/python3
"""My Script."""

import requests


def number_of_subscribers(subreddit):
    """docs."""
    myheader = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, myheaders=myheader, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
