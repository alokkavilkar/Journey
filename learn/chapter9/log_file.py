# Write a Python program that reads a log file (access.log) containing HTTP access logs and performs the following operations:

# Count the number of unique IP addresses accessing the server.
# Identify the top 5 most visited URLs.
# Calculate the total number of requests per HTTP status code.
# Generate a report summarizing the findings.

import re
from collections import Counter

fileName = 'access.log'

def find_ips(file, ips):

    with open(file, 'r') as f:

        for line in f:
            ip = line.split(' - ')
            ips.add(ip[0])

    return ips

def status_code_per (file, list):
    ans_dict = {}
    with open(file, 'r') as f:

        for line in f:
            data = line.split(' ')
            print(data[8])
            if ans_dict.get(data[8]) != None:
                ans_dict[data[8]] = ans_dict.get(data[8]) + 1
            else:
                ans_dict[data[8]] = 1
        
        return ans_dict

ips = find_ips(fileName, set())
# print(ips)

dict = status_code_per(fileName, list)
print(dict)

