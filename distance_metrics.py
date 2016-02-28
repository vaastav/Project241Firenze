# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 05:07:39 2016

@author: sssonalee
"""
from scipy.spatial.distance import hamming
from scipy.spatial.distance import euclidean
import numpy as np

def conditional_euclidean_distance (values1, values2):
	if hamming(values1, values2) == 0: 
		return 0

	else:
		return euclidean(values1, values2)/hamming(values1, values2)

#arr = np.array([1, 1.6, 2.4, 3.6, 5.2, 6.6, 8, 9.2, 10])
#arr2 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 10])
#print (conditional_euclidean_distance(arr, arr2))