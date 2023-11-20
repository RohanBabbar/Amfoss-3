t = int(input())

if t>=1 and t<=10:
    
    for i in range(t):
        n=int(input())
        x = 2
        while x * x <= n:
            if n % x == 0:
                n //= x
            else:
                x += 1
        print(n)