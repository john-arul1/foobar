# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:25:20 2024

by John Arul

Foobar problem counting orbits  of matrix permutation groups

"""

'''
steps
1. enumerate group size

2. use Cauchy-Frobenius lemma   orbits M * |G|  =  Sum(g in G) |fix(g)| 
= Sum (i) |Ci| |fix(gi)| with gi a representative of class Ci

|fix(g)|  depends on the cycle structure of g


s^(m rows or n cols)^

N - number of cycles in g  = partition length

# not used
P - number of distinct partitions of integer Z
P(Z)= P(Z-1)+P(Z-2)-P(Z-5)-P(Z-7)....
used to estimate C(g)
#
generate set of distinct partitions

equivalence class for N
C(N)(l=1..N) = N!/(prod(pj)*multip(pj)!) j = 1..l 


'''




def factorial(l):
    #return math.factorial(l)
    
    if l<=0:
       return int(1)
    else: 
       return l*factorial(l-1) 
        

def group_size(m,n):
    #|G|
    return factorial(m)*factorial(n)


# def set_size(m,n,s):
#     #|Omega|
#     return s**(m*n)
    
def mod(a,b):
    return (a-(a//b)*b)    
    
def gcd(a,b):
    if a < b:
       x=a
       a=b
       b=x
    
    while mod(a,b) != 0:
        c=mod(a,b)
        a=b
        b=c
    return b 
    
def multiplicity(part):
    # returns dictionary of multiplicity of cycles
    count={}
    for num in part:
        if num not in count:
           count[num]=0
        count[num]+=1
    
    return count 
 
            
def partitions(number):
        part = set()
        part.add((number, ))
        for x in range(1, number):
           for y in partitions(number - x):
                part.add(tuple(sorted((x, ) + y)))
        return list(part)            


def num_permutations(part):
    vsum=sum(part)  
    #handle specila cases- though not essential
    if len(part) == 1:
       v=factorial(vsum-1) 
       return v
   
    if len(part) == vsum:
        return 1
    
    prod=1.0
    for v in part:
        prod*=v
        
    res=factorial(vsum)/prod
    
    # get multiplicity
    freq_dict=multiplicity(part)
     
    fact =1
    for v in freq_dict.values():
        fact*=factorial(v) 
    
    #print(part,freq_dict,res,fact)
    res=res/fact
    
    return res



def cycles_class_size(Z):
    # Z = m or n
    # List of number of permutations of cycles of length 1 to Z with repetitions
    C={}
       
    part_list=partitions(Z)
    np=0
        
    for part in part_list:
        np =num_permutations(part)
        
        C[part]=int(np)        
        
    return C
       

def get_exponent(part):
    #exponent for product terms
    x,l1,l2=part
    gd=0
    for n1 in l1:
        for n2 in l2:
            gd+=gcd(n1,n2)
    return gd



def solution(n,m,s):

        #identity
        F={}  # Fix(g)
        
        #column permutation with identity
        Cc=cycles_class_size(n)
        for part in Cc.keys():  # number of cycles
             F[('c',part)]= Cc[part]*s**(m*len(part))
        
        #row permutation
        Cr=cycles_class_size(m)
        for part in Cr.keys():  # number of cycles
            if len(part)< m: #exclude identity 
                F[('r',part)]= Cr[part]*s**(n*len(part))
        
        #product permutation
        Cprod={}
        for part_c in Cc.keys():  # number of cycles
            if len(part_c) < n: # identity excluded
               for part_r in Cr.keys():
                  if len(part_r) < m: 
                     Cprod[('p',part_r,part_c)]=Cc[part_c]*Cr[part_r] 
                   
        for part in Cprod.keys():  # number of cycles
            p=get_exponent(part)
            F[part]= Cprod[part]*s**p
        
        
        M=sum(F.values())//group_size(m,n)
        return str(M)

        
        
        # check group size
        #print(sum(Cr.values())+sum(Cc.values())+sum(Cprod.values())-1,group_size(m,n))
        
        

print('orbits',solution(2,3,4))

# print(Cprod)
# print('\n')   
# print(F)
# print(sum(F.values()))
    

# m=5    
# x=cycles_class_size(m)

# print(x)    
# print(math.factorial(m),sum(x.values()))    
    
# y=123456789123456789111

# print(y+2)

# import math
# for i in range(15):
#     if factorial(i) != math.factorial(i):     
#         print(i,factorial(i),math.factorial(i))




