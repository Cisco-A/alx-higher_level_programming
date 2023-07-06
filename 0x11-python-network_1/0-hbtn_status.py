#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
    print(
        f"Body response:$\n    - type: {type(html)}$\n    - content: {html}$\n    - utf8 content: {html.decode('utf8')}$")
