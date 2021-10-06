#!/usr/bin/python3
""" Module that prints mesage with first name and last name """


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>

    Args:
    first_name: string
    last_name: string

    Returns:
    Void

    Raises:
    - first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message first_name must be a string
    or last_name must be a string
    """
    message = "My name is {first_name} {last_name}"
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(message.format(first_name=first_name, last_name=last_name))

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
