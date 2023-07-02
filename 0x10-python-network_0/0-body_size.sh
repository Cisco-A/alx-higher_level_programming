#!/bin/bash
# Send a request to a URL and display the body size of the response
curl -s -o /dev/null -w '%{size_download}\n'
