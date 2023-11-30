#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-