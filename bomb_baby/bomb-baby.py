# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:27:00 2023

@author: John

M--> M+F
or

F--> F+M

Problem was not described clearly had to look at google

Answers were shown as integers. But to be returned as str causing initial test failures

"""


def solution(x, y):
    # Your code here
    steps=0
    
    M=int(x)
    F=int(y)
    
    while True:

        if M == 1 and F == 1:
            if steps >=1:
                return str(steps)
            else:
                return 'impossible' #zero steps not possible?           
        
        if (M == F) or (M <= 0) or (F <= 0):
            return "impossible"
        
        if M > F:
            d=(M-1)//F 
            M= M-d*F
            steps=steps+d
        else:
            d=(F-1)//M
            F=F-d*M
            steps=steps+d
    
    