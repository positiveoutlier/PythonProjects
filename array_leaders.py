# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:56:22 2019

@author: positiveoutlier

An element is a leader if it is greater than the sum of all the elments to
its right side. Given an input list with integers, returns a list with leaders.
Expected input:  list with integers
Expected output: list with integers
"""


def array_leaders(numbers):
    leaders = []
    for index in range(len(numbers)):
        if numbers[index] > sum(numbers[(index+1):]):
            leaders.append(numbers[index])
    return leaders


array_leaders([16, 17, 4, 3, 5, 2])


# Using list comprehension in combination with enumerate

def array_leaders2(numbers):
    return [n for (i, n) in enumerate(numbers) if n > sum(numbers[(i+1):])]


array_leaders2([16, 17, 4, 3, 5, 2])
