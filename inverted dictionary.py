# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:15:11 2019

@author: positiveoutlier
"""


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary where the keys are the unique values
    of the original dictionary. The value for a key in the inverse dictionary
    is a sorted list of all keys in the original dictionary that have the
    same value in the original dictionary.

    Examples:
    d = {1:10, 2:20, 3:30, 4:30} --> dict_invert(d) returns
        {10: [1], 20: [2], 30: [3, 4]}
    d = {4:True, 2:True, 0:True} --> dict_invert(d) returns {True: [0, 2, 4]}
    '''
    invDict = {}
    for k in d:
        if d[k] not in invDict:
            invDict[d[k]] = [k]
        else:
            invDict[d[k]].append(k)
            invDict[d[k]].sort()
    return invDict


print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({30000: 30, 600: 30, 2: 10}))
