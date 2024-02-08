#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lght = len(my_list)
    if idx > lght - 1:
        return my_list
    elif idx < 0:
        return my_list
    del my_list(idx)
