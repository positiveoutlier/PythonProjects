# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:07:37 2019

@author: positiveoutlier
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        for i in range(2, exp):
            base *= base
        return base

iterPower(30, 0)