#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if my_list[i] != None and type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            else:
                continue
        print()
        return (count)
    except Exception:
        pass
