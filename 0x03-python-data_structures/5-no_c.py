#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        n_string = my_string.translate({ord("c"): None})
        s_string = n_string.translate({ord("C"): None})
        return s_string
    return my_string