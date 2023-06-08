#!/usr/bin/python3
x = 0
letters = ord('z')

while letters >= ord('a'):
    print("{}".format(chr(letters - x)), end="")
    x = 32 if x == 0 else 0
    letters -= 1
