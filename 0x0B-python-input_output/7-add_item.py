#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()
        if len(split_line) > 2:
            if split_line[-2] in status_codes:
                status_codes[split_line[-2]] += 1
            total_size += int(split_line[-1])
        if count == 10:
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            count = 0
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
    sys.exit(0)
