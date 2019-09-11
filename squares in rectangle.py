# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:25:08 2019

@author: positiveoutlier

Provides the dimensions of each of the squares if a true rectangular is cut in
squares. A rectangular is true if the width does not equal the length.
Expected input:  - positive integer lenght (lng)
                 - positive integer width (wdth)
Expected output: - array with the size of each quarters
                 - None if the rectangular is not true
"""


def sqInRect(lng, wdth):
    '''
    The solution below is a greedy solution and will not always produce
    an optimal solution.
    '''
    if lng == wdth:
        return None
    dimensions = []
    while lng != 0 and wdth != 0:
        number = max(lng, wdth) // min(lng, wdth)
        for i in range(number):
            dimensions.append(min(lng, wdth))
        if wdth > lng:
            wdth, lng = lng, wdth
        lng = lng - (wdth * number)
        return dimensions


sqInRect(36, 30)