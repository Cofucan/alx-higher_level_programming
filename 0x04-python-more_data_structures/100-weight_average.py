#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0
    for tup in my_list:
        total_score += tup[0] * tup[1]
        total_weight += tup[1]

    return total_score / total_weight
