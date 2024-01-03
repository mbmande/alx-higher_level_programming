#!/usr/bin/python3
for ft in range(0, 10):
    for sd in range(ft + 1, 10):
        if ft == 8 and sd == 9:
            print("{}{}".format(ft, sd))
        else:
            print("{}{}, ".format(ft, sd), end='')
