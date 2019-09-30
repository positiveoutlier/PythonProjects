# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:46:58 2019

@author: positiveoutlier
"""

""" t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """


def max_val(List):
    global result
    result = []
    return _flatten(List)


def _flatten(List):
    global result
    for item in List:
        if type(item) == list or type(item) == tuple:
            _flatten(item)
    else:
        result.append(item)
    return result


print(max_val(((-10, 91), [[5], [100, 25]])))