'''
john arul, 14/11/23
'''

import math

def diff(a,b):
    c=[0,0]
    c[0]=b[0]-a[0]
    c[1]=b[1]-a[1]

    return c


def dist(p):
    return p[0]**2+p[1]**2

def dist2(p1,p2):
    #print(d)
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


def gcd(a,b):
    a=abs(a)
    b=abs(b)
    if b:
        return gcd(b, a % b);
    else:
        return a
        

def dcs(p1,p2):
    delta=diff(p1,p2)
    na=[0,0]    
    ga=gcd(delta[0],delta[1])
    if ga==0: return (0,0)
    na[0]=delta[0]/ga
    na[1]=delta[1]/ga
    return  (na[0],na[1])
       
             

def solution(dim,gun,target,length):
        
    sim_list=[]
    tim_list=[]
    cim_list=[] 
    tim_list_acc=[]
    
    cim_dcs={(0,0):0}
    sim_dcs={(0,0):0}
    
    
    n=math.ceil(float(length)/dim[0])
    m=math.ceil(float(length)/dim[1])
    
    n=int(n)
    m=int(m)
              
    Lx=list([x-n for x in range(2*n+1)])
    Ly=list([y-m for y in range(2*m+1)])
        
    
    for i in Ly:
        for j in Lx:
           
           #shift
           if j %2 ==0:
               x=target[0]+j*dim[0]
           else:
               x=(j+1)*dim[0]-target[0]

           if i% 2== 0:    
               y=target[1]+i*dim[1]
           else:
               y=(i+1)*dim[1]-target[1]

           p=(x,y)
           d=dist2(gun,p)
           if  d <= length**2: 
               tim_list.append(p)  # coordinate
                        
           
           #source image list
           if j %2 ==0:
               x=gun[0]+j*dim[0]
           else:
               x=(j+1)*dim[0]-gun[0]

           if i% 2== 0:    
               y=gun[1]+i*dim[1]
           else:
               y=(i+1)*dim[1]-gun[1]

           p=(x,y)
           d=dist2(gun,p)
           if  d <= length**2:
                 sim_list.append(p)  # coordinate
                  
           # corner image list 
           x=j*dim[0]
           y=i*dim[1]
           p=(x,y)
           d=dist2(gun,p)
           if  d <= length**2: 
               cim_list.append(p)  # coordinate
                      
    cim_list.sort(key=dist)    
    tim_list.sort(key=dist)   
    sim_list.sort(key=dist)    
     
    
    for p in sim_list:
        d=dist2(gun,p)
        z=dcs(gun,p)
        if z not in sim_dcs:
            sim_dcs.update({z:d})
        elif sim_dcs[z] > d:
             sim_dcs.update({z:d})

    for p in cim_list:
        d=dist2(gun,p)
        z=dcs(gun,p)
        if z not in cim_dcs:
            cim_dcs.update({z:d})
        elif cim_dcs[z] > d:
             cim_dcs.update({z:d})
            
    
    # filter              
    tim_list1=[]
    for tim in tim_list: #remove direction to corner img
        
        dt=dist2(gun,tim)
        z=dcs(gun,tim)
        #print(cim,corner_dcs) 
        if z in cim_dcs:
            dc=cim_dcs[z]
            if dc > dt:
               tim_list1.append(tim) 
        
        else:
           tim_list1.append(tim)
    
    tim_list2=[]
    for tim in tim_list1: #remove direction to corner img
        
        dt=dist2(gun,tim)
        z=dcs(gun,tim)
        #print(cim,corner_dcs) 
        if z in sim_dcs:
            ds=sim_dcs[z]
            if ds > dt:
               tim_list2.append(tim) 
        
        else:
           tim_list2.append(tim)
    
    tim_dcs={}
    for im in tim_list2:
        z=dcs(gun,im)
        tim_dcs.update({z:0})

    k=len(tim_dcs)
                   
    return k