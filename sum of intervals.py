# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:32:53 2019

@author: positiveoutlier

This function accepts an array of intervals, and returns the sum of all the
interval lengths. Overlapping intervals should only be counted once.
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5.
The length of this interval is 4.

Expected input: a list of lists, with each sublist consisting of two integers
Expected output: an integer, the sum of the intervals in the list of lists
"""


def sum_of_intervals(intervals):
    result = 0
    for i in range(len(intervals)):
        result += intervals[i][1] - intervals[i][0]
    return result


'''
Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
'''
