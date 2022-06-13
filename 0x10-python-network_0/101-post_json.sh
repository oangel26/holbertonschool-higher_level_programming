#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument
curl -sH "Content-Type: application/json" -d @"$2" "$1"
