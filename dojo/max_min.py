# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:18:33 2021

@author: yeshw
"""

"""
Your task is to make two functions, max and min 
(maximum and minimum in PHP and Python) that take a(n) array/vector of 
integers list as input and outputs, respectively, the largest and lowest 
number in that array/vector.

#Examples

maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0
#Notes
You may consider that there will not be any empty arrays/vectors.
"""

#returns the min element from the list
def minimum(arr):
    return min(arr)

#returns the max element from the list
def maximum(arr):
    return max(arr)

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([-52, 56, 30, 29, -54, 0, -110]))