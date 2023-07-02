#!/bin/bash
# Display the body of a JSON POST request
curl -s -F "name=@$2" "$1"
