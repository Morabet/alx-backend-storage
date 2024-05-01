#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    """
    function uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """

    value = "count:{}{}{}".format('{', url, '}')
    r.incr(value)
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')
    res = requests.get(url)
    html_content = res.text
    r.setex(url, 10, html_content)
    return html_content
