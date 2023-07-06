#!/usr/bin/python3
"""A python script that takes a URL and returns its
   X-Request-Id variable found in the header of the response.
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        content = response.headers

    print(content.get("X-Request-Id"))
