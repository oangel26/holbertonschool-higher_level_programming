#!/usr/bin/python3
""" Show headers"""
import urllib.request
import urllib.parse
from sys import argv
from urllib import parse
if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = {'email': email}
    data = parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
        
