#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argumen
curl -sw "%{http_code}" "$1" -o /dev/null
