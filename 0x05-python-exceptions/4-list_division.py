#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) and my_list_2[i] != 0 else 1
            division_result = dividend / divisor
        except IndexError:
            print("out of range")
            continue
        except ZeroDivisionError:
            print("division by 0")
            return None
        except TypeError:
            print("wrong type")
            return None
        else:
            result.append(division_result)

    return result
