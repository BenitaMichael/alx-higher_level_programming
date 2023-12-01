#!/bin/bash
# sends a JSON POST request to a URL, and displays the body of the response
curl -sXH -d "$(cat"$2")" "$1" POST  "Content-Type: application/json""$1"