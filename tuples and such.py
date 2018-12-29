# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:39:00 2018

@author: positiveoutlier
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oddTuple = ()
    for index in range(len(aTup)):
        if index % 2 == 0:
            oddTuple = oddTuple + aTup[index : (index + 1)]
    return oddTuple

oddTuples(('I', 'am', 'a', 'test', 'tuple'))
