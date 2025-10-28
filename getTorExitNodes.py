#! /usr/bin/env python3 

import urllib.request
from bs4 import BeautifulSoup
import re
import sys

def print_help():
    print(f"""
    ...::: getTorExitNodes :::...

Usage: python3 getTorExitNodes.py [OPTIONS] 

Options: \t 
    -v, --verbose Verbose output: print IP's to terminal\t 
    -h, --help Show this help message
    """)

verbose = False
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg in ("-v", "--verbose"):
        verbose = True
    elif arg in ("-h", "--help"):
        print_help()
        sys.exit(0)
    else:
        print(f"Unknown argument: {arg}, try -h or --help for help.")
        sys.exit(0)

print(f"Connecting to TorProject")
url = "https://check.torproject.org/exit-addresses"

print(f"Fetching exit node list")
get_url = urllib.request.urlopen(url).read()
get_soup = BeautifulSoup(get_url, 'lxml')

print(f"Parsing node list and saving to ips.txt")
get_body = get_soup.body.text
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

with open("ips.txt", "w") as file:
    for line in get_body.splitlines():
        match = ip_pattern.search(line)
        if match:
            if verbose:
                print(match.group())
            file.write(match.group() + "\n")

print("Done")
