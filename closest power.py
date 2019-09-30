# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 07:09:26 2019

@author: positiveoutlier
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    for exp in range(100000000):
        if base ** exp <= num and base ** (exp + 1) >= num:
            break
        else:
            exp += 1
    if (abs(num - base ** exp)) <= abs(base ** (exp + 1) - num):
        return exp
    else:
        return exp + 1


print(closest_power(3, 12))
print(closest_power(4, 12))
print(closest_power(4, 1))
print(closest_power(10, 900))
print(closest_power(4, 37))
   