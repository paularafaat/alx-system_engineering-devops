#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Function to return the first 10 hot posts listed
      for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditScript/1.0 (by u/paula)"
    }
    params = {
        'limit': 10
    }
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']["children"]
        titles = [post['data']["title"] for post in hot_posts]
        for title in titles[:10]:
            print(title)
    else:
        print(None)
        return
