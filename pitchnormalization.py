# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:01:25 2016

@author: sssonalee
"""
from scipy.signal import medfilt
import numpy as np
from scipy.stats.mstats import zscore

def median_filter(values, window_size):
    return medfilt(values, window_size)
    
def average_filter(values, window_size):
    for i in range(int((window_size-1)/2)):
        values = np.insert(values,0,values[0])
        values = np.append(values,values[len(values)-1])
    return np.convolve(values, np.ones(window_size) / window_size, mode='valid')

def filter_one_d_array(values, window_size):
    return average_filter(median_filter(values, window_size),window_size)
    
def zscorenormalize(values):
    return zscore(filter_one_d_array(values,5))
    

# tests and chill    
arr = np.array([0, 2, 3, 3, 4, 6, 10, 15, 97])
arr2 = [2, 80, 6, 3] 
print (median_filter(arr, 5))
print (filter_one_d_array(arr,5))
print (zscorenormalize(arr))