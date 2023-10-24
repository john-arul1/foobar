def solution(n):
    # Your code here
    n=int(n)
    steps=0
    while(n!=1):        
        if n%2 == 0:
            n=n/2
        elif n==3 or n%4==1:        
            n=n-1
        else:
            n=n+1
            
        steps=steps+1

    return str(steps)        
        



print(solution('24'))