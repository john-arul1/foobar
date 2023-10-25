# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:39:57 2023

@author: John Arul

Bunny worker locations:

Solution: Cantor's enumeration formula

"""

def solution(x, y):    
    # Your code here
    if y>1: 
       k=y-2
    else:
       k=0
       
    v=x*(x+1)/2+(y-1)*x+k*(k+1)/2
    return str(v)


print(solution(5,10))
