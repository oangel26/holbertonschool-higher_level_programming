#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of the string, removing the character at the position n"""
    cpy = str[:]
    if n >= 0:
        return cpy[0: n] + cpy[n + 1:]
    else:
        return cpy
 
