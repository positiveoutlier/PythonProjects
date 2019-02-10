# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:45:00 2019

@author: positiveoutlier
"""
s = 'azcbobobegghakl'

vowels = 0
for letter in s:
    if letter in ("aeiou"):
        vowels += 1

print("Number of vowels: " + str(vowels))
