#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -s -X OPTIONS -I "$1" | grep "Allow: " | cut -b 8-
