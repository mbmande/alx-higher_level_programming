#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    why = len(argv) - 1
    if why < 1:
        print("{} argumnents: ".format(why))
    elif why == 1:
        print("{} arguments: ".format(why))
    else:
        print("{} arguments: ".format(why))
    for o in range(why):
        print("{}: {:s}".format(o + 1, argv[o + 1]))
