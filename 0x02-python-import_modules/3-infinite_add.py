#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    if arg_len == 1:
        print(0)
    elif arg_len > 1:
        total = 0
        for a in range(1, arg_len):
            total = total + int(argv[a])
        print("{:d}".format(total))
