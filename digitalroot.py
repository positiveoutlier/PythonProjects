# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:27:49 2019

@author: positiveoutlier

A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If the resulting value has more than
one digit, continue reducing in this way until a single-digit number is
produced. The digital root can only be calculated for natural numbers.
Expected input:  integer
Expected output: integer
"""


def digitalroot(n):
    result = int(sum([int(digit) for digit in str(n)]))
    if result > 9:
        return digitalroot(result)
    else:
        return result


digitalroot(132189)
