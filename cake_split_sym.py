# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:10:45 2023

@author: John

google challenge split cake into equal parts.

extract number of full identical substrings

"""


def shift_compare(s,n):
    # rotate and compare
    N=len(s)
    
    equal=True
    for i in range(len(s)):
        if s[i]!= s[(i+n)%N]:    
           equal =False
           break
    return equal     
    

def solution(s):
    
    # 
    for i in range(1,len(s)):
         
        #if i devides len(s)
        N=len(s)
        if (abs(N/i-N//i) ==0):
            if shift_compare(s,i):
               return N//i 
            
    return 1
        
        
          
#s="abcdabcdabcd"
s="abccbaabccba"
#s='abcabcabcabcabc'
#s='abcdefghijkl'
#s=random.choices("abc", k=7)
# z=''
# for i in range(10):
#       z+=s
z=s    
print(len(z))    
d=solution(z)
print (d)        