#!/usr/bin/python3
""" Show headers"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
        
