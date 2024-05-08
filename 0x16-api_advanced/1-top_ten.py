#!/usr/bin/python3
"""My Script."""

import requests


def top_ten(subreddit):
    """docs."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    myCustomAgent = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=myCustomAgent, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
