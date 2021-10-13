#!/usr/bin/python3
"""Module that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after
    each line containing a specific string
    """
    file_lines = []
    with open(filename, 'r+', encoding="UTF8") as f:
        line = f.readline()
        file_lines.append(line)
        while line:
            file_lines.append(line)
            if  search_string in line:
                file_lines.append(new_string)
            line = f.readline()
        f.seek(0, 0)
        f.writelines(file_lines)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
