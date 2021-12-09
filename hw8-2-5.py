# Author: SCT (AMDG) 12/9/21

def sum_even(lst):

    number = 0

    for x in lst:
        if x % 2 != 0:
            break
        else:
            number += x
    return number

print(sum_even([2, 4, 6, 8, 9]) == 20)
print(sum_even([13, 12, 10]) == 0)
print(sum_even([14, 16, 32]) == 62)

