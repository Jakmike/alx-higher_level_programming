#!/usr/bin/python3
def safe_print_integer(value):
    i = value
    if value is True:
        print("{:d}".format(i))
        return True
    else:
        return False
