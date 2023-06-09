#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = len(sys.argv) - 1

if argv == 0:
    print("{} arguments.".format(argv))
elif argv == 1:
    print("{} argument:".format(argv))
else:
    print("{} arguments:".format(argv))
for x in range(1, argv + 1):
    print("{}: {}".format(x, sys.argv[x]))
