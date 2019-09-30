# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 07:46:31 2019

@author: positiveoutlier
"""


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    for item in range(len(L) - 1, -1, -1):
        newList = []
        for value in range(len(L[item]) -1, -1, -1):
            newList.append(L[item][value])
        L.remove(L[item])
        L.append(newList)
    return L


#print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))
#print(deep_reverse([[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]))
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)