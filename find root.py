# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:03:48 2019

@author: positiveoutlier
"""


def findRoot(x, power, epsilon):
    """ Assumes x and epsilon int or float, power an int,
        epsilon > 0 & power >= 1
        Returns float y such that y**power is within epsilon of x.
        If such a float does not exists, it returns None."""

    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return print(ans)


findRoot(-32, 5, 0.0001)