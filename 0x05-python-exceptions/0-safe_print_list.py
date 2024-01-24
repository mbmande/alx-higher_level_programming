#!/usr/bin/python3

'''it prints the value of x
Arags:
    my_list (list): its printed from this list
    x (int): the amount to be printed


Returns:
    the amount that us printed
    '''


def safe_print_list(my_list=[], x=0):
    mande = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            mande += 1
        except IndexError:
            break
    print("")
    return (mande)
