#!/usr/bin/python3
def raise_exception():
    """ Function that raises a type exception """
    raise TypeError

if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
        
