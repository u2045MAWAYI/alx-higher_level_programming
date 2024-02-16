#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 0
    for element in my_list:
        if count == idx:
            return element
        count += 1
    return None
