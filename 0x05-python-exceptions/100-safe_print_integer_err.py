#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise TypeError("Value is not an integer")
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
