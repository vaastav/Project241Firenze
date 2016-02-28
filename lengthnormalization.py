# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:01:04 2016

@author: Sultan
"""

import numpy as np

def normalize_length(twodarray, coefficient_and_max_length):
    coefficient = coefficient_and_max_length[0]
    length = 0
    for row in twodarray:
        length += row[1]
    if length == coefficient_and_max_length[1]:
        coefficient = 1
    onedarray = np.array([])
    for row in twodarray:
        for i in range(row[1]*coefficient):
            onedarray = np.append(onedarray,row[0])
    tempArrayLength = len(onedarray)
    if tempArrayLength < coefficient_and_max_length[1]:
        number_to_add = coefficient_and_max_length[1] - tempArrayLength
        if number_to_add % 2 == 0:
            for i in range(number_to_add // 2):

                onedarray = np.insert(onedarray,0,onedarray[0])
                onedarray = np.append(onedarray,onedarray[len(onedarray)-1])
        else:
            for i in range(number_to_add // 2):
                print(onedarray)
                onedarray = np.insert(onedarray,0,onedarray[0])
                onedarray = np.append(onedarray,onedarray[len(onedarray)-1])
            onedarray = np.insert(onedarray,0,onedarray[0])
    elif tempArrayLength > coefficient_and_max_length[1]:
        number_to_remove = tempArrayLength - coefficient_and_max_length[1]
        if number_to_remove % 2 == 0:
            for i in range(number_to_remove // 2):
                onedarray = np.delete(onedarray, 0)
                onedarray = np.delete(onedarray, len(onedarray)-1)
        else:
            for i in range(number_to_remove // 2):
                onedarray = np.delete(onedarray, 0)
                onedarray = np.delete(onedarray, len(onedarray)-1)
            onedarray = np.delete(onedarray, 0)
    return onedarray
    
def get_coefficient(twodarray1, twodarray2):
    length1 = 0
    for row in twodarray1:
        length1 += row[1]
    length2 = 0
    for row in twodarray2:
        length2 += row[1]
    coefficient = 1
    if length1 > length2:
        coefficient = (length1 + length2 //2) // length2
    elif length2 > length1:
        coefficient = (length1 + length2 //2) // length1
    coefficient_and_max_length = np.array([coefficient,max(length1,length2)])
    return coefficient_and_max_length

# examples
# exarray1 = np.array([[6,6],[3,4],[9,7]])
# exarray2 = np.array([[2,2],[7,1],[6,3]])

# print(exarray1)
# print(exarray2)

# coefficient_and_max_length = get_coefficient(exarray1, exarray2)
# print(coefficient_and_max_length)

# print(normalize_length(exarray1,coefficient_and_max_length))
# print(normalize_length(exarray2,coefficient_and_max_length))
