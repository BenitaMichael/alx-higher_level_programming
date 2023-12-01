#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
<<<<<<< HEAD
curl -s "$1" | wc -c
=======
curl -I -s "$1" | grep "Content-Length:" | cut -d " " -f 2
>>>>>>> 69bad030e30d7b9939a4ba5577a8c004b08bb044
