#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function that returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    if my_list == [] or my_list is None:
        return 0
    else:
        tuple_score = 0
        tuple_weight = 0
        for tupl in my_list:
            tuple_score = tuple_score + (tupl[0] * tupl[1])
            tuple_weight = tuple_weight + tupl[1]
        return tuple_score / tuple_weight

if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
