#!/usr/bin/python3
def uppercase(str):
    for up in str:
        if ord(up) >= ord('a') and ord(up) <= ord('z'):
            up = chr(ord(up) - 32)
        print("{:s}".format(up), end="")
    print()
