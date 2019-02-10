# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:50:28 2018

@author: positiveoutlier
"""

s = 'bobobobobobobobobob'
bob_counter = 0
for index in range(len(s)):
    if index + 3 <= len(s):
        if s[index: (index + 3)] == "bob":
            bob_counter += 1

print("Number of times bob occurs is: " + str(bob_counter))
