#!/usr/bin/python3
def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result."""
    try:
        result = a / b
        return (result)
    except:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))

if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
