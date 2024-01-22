#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, a = 0, o
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            a += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return a