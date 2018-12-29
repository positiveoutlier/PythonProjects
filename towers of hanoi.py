# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:23:56 2018

@author: positiveoutlier

code copied from https://en.wikipedia.org/wiki/Tower_of_Hanoi [28/5/2018]
made the following changes:
    - number of disks in function call can vary without having to make any other code changes
    - print the starting position of the towers
"""

def starting_point(disks):
    global first_tower, extra_tower, target_tower
    
    first_tower = list(range(disks, 0, -1))
    extra_tower = []
    target_tower = []
    print("Starting point:")
    printGlobals()
    move(disks, first_tower, target_tower, extra_tower)
    
    
def move(n, source, target, auxiliary):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(n)
        printGlobals()

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)

def printGlobals():
        print("Source:  ", first_tower)
        print("Support: ", extra_tower)
        print("Target:  ", target_tower)
        print('##############')
    
        
starting_point(3)


