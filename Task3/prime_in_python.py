def printPrime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if (num%i)==0:
            return False
        else:
            return True
print("Enter n")
num = int(input())
for i in range(2,num+1):
    if printPrime(i):
        print(i,end=",")