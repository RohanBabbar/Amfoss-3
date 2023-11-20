t=int(input())
for i in range (0,t):
    n=int(input())
    n1,n2=1,2
    y=2
    while n1+n2<n:
        
        nth= n1 + n2
        n1=n2
        n2=nth
        if nth%2==0:
            y=y+nth
        
    if n>1:       
        print(y)
    else:
        print(0)