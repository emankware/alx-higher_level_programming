#!/usr/bin/python3

if__name__ == "__main__":
    from sys import argv
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for w in range(count):
        print("{}: {}".format(w + 1, sys.argv[w + 1]))
