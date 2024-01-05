#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    con = dir()
    for i in range(0, len(con)):
        if con[i][:2] != "__":
            print("{:s}".format(con[i]))
