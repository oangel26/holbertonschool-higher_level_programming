#!/usr/bin/python3
"""Program that prints all the names defined by the compiled module"""
if __name__ == "__name__":
    import hidden_4
    for i in dir(hidden_4):
        if i[0:2] != "__":
            print(i)
