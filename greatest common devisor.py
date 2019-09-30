# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:06:42 2019

@author: positiveoutlier
"""


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    iterative method
    '''
    low = min(a, b)
    for i in range(low, 0, -1):
        if i == 1:
            return i
        elif a % i == 0 and b % i == 0:
            return i


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    recursive method (based on Euclidean algorithm)
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
