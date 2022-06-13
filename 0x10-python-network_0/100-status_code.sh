#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argumen
curl -so /dev/null -sw "%{http_code}" "$1"
