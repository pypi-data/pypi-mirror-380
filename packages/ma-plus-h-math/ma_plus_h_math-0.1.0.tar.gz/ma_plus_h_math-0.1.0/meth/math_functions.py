"""
Mathematical functions module for ma+h library
"""

import math


def sine(x):
    """
    Calculate the sine of an input value.
    
    Args:
        x (int or float): Input value in radians
        
    Returns:
        float: The sine value of the input
        
    Example:
        >>> sine(0)
        0.0
        >>> sine(math.pi/2)
        1.0
    """
    return math.sin(x)
