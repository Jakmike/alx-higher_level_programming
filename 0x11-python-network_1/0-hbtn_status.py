#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
response = urllib.request.urlopen(url)
if response.status == 200:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
