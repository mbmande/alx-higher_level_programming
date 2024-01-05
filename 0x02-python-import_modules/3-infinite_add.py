#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    mande = 0
    for i in range(1, len(argv)):
        mande += int(argv[i])
    print("{}".format(mande))
