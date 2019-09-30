# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:22:55 2019

@author: positiveoutlier
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

Examples:
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains more than 3 numbers.
The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
