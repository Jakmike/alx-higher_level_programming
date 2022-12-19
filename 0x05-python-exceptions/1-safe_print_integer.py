#!/usr/bin/python3
def safe_print_integer(value):
    i = value
    try:
        print("{}".format(i))
        return True
    except value is True:
        return False
