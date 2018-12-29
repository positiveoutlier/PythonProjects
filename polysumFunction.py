# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:55:18 2018

@author: positiveoutlier
"""

def polysum(n, s):
    """
    n: number of sides
    s: side length

    Returns: The sum of area and perimeter**2 of the regular polygon defined by n and s,
    rounded to 4 decimal places.
    """
    
    # Import pi and tan from math module
    from math import pi, tan
    
    # Calculate the area
    area = (0.25 * n * s ** 2) / tan(pi / n)
    
    # Calculate the perimeter
    perimeter = (s * n)
    
    # Return the sum of the area and the perimeter squared, rounded to 4 decimals
    return round(area + perimeter**2, 4)
