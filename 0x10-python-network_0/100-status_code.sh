#!/bin/bash
# Return only the status code of a response
curl -I -s -o /dev/null -w "%{http_code}" "$1"
