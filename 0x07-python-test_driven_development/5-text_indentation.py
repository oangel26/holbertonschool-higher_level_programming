#!/usr/bin/python3
""" Module that print text """


def text_indentation(text):
    """ Function that prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
    text: string

    Returns:
    Void

    Raises:
    - text must be a string, otherwise raise a TypeError
    exception with the message text must be a string.

    - There should be no space at the beginning or at the
    end of each printed line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    switch = 0
    for i in range(len(text)):
        if ord(text[i]) == 32 and switch == 1:
            continue
        else:
            switch = 0
        if switch == 0 and ord(text[i]) == 32 and ord(text[i + 1]) == 32:
            continue
        print("{}".format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
            switch = 1


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")


