#!/usr/bin/python3
def no_c(my_string):
    """Function that removes all characters c and C from a string."""
    new_str = ""
    for i in my_string:
        if i == "c" or i == "C":
            pass
        else:
            new_str += i
    return new_str

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
    
