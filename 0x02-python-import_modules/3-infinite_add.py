#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    _len = len(argv)
    if _len == 1:
        print(0)
    elif _len > 1:
        total = 0
        for a in range(1, _len):
            total = total + int(argv[a])
        print("{:d}".format(total))
