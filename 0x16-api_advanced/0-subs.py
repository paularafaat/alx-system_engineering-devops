#!/usr/bin/python3
"""
    uses reddit api to print num of sub
"""
import requests


def number_of_subscribers(subreddit):
    """
        get the num of sub
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
