#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    number = 0
    for i in range(count):
        number += int(sys.argv[i + 1])
    print("{}".format(number))
