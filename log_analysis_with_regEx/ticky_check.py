!#/usr/bin/env python3

import re
import sys
import os

user_errors = {}
user_info = {}

file = r"syslog.log"

f = open(file, 'r')

errorfile = 'error_message.csv'
userfile = 'user_statistics.csv'

for log in f:
    result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
    if result.group(2) not in user_errors.keys():
        user_errors[result.group(2)] = 0
    user_errors[result.group(2)] += 1
    if result.group(3) not in user_info.keys():
        user_info[result.group(3)] = {}
        user_info[result.group(3)]["INFO"] = 0
        user_info[result.group(3)]["ERROR"] = 0

    if result.group(1) == "INFO":
        user_info[result.group(3)]["INFO"] += 1
    elif result.group(1) == "ERROR":
        user_info[result.group(3)]["ERROR"] += 1


user_errors = sorted(user_errors.items(), key = operator.itemgetter(1), reverse = True)
user_info = sorted(user_info.items())

f.close()

user_errors.insert(0, ('Error', 'Count'))

f = open(errorfile, 'w')
for error in user_errors:
    a,b = error
    f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(userfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in user_info:
    a,b = user_stats
    f.write(str(a)+','+str(b["INFO"])+','str(b["ERROR"])+'\n')
