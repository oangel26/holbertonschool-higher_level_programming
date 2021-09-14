#!/usr/bin/python3
def multiple_returns(sentence):
    """Function that returns a tuple with the length of a
    string and its first character.
    """
    if sentence[0] == None:
        sentence_tuple = 0, None
    else:
        sentence_tuple = len(sentence), sentence[0]
    return sentence_tuple

if __name__ == "__main__":
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
