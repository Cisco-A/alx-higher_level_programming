#!/bin/bash
# Send a POST request and disiplay the body of the response
curl -s -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
