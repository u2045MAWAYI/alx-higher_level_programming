#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score_sum = 0
    total_weight_sum = 0

    for score, weight in my_list:
        total_score_sum += score * weight
        total_weight_sum += weight

    weighted_average = total_score_sum / total_weight_sum

    return weighted_average
