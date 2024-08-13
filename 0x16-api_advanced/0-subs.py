#!/usr/bin/python3
"""subs module"""
import requests


def number_of_subscribers(subreddit):
    """Function to return the num of sub"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "MyRedditScript/1.0 (by u/paula)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json()
    return data["data"]["subscribers"]
