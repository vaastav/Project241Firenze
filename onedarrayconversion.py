# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:01:04 2016

@author: Sultan
"""

import numpy as np

def convert(twodarray):
    onedarray = np.array([])
    for row in twodarray:
        for i in range(row[1]):
            onedarray = np.append(onedarray,row[0])
    return onedarray
    
""" examples
exarray = np.array([[6,6],[3,4],[9,7]])

print(exarray)

print(convert(exarray))
"""