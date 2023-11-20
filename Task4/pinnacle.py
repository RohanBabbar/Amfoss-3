n = int(input())
for i in range(n):
    [l, r] = input().strip().split(' ')
    if l==r:
        print(0)
        continue
    l = "0"*(len(r)-len(l)) + l
    x = 0
    for j in range(len(r)):
        if l[j] != r[j]:
            
            break
        x += 1
    res = (len(r)-x-1)*9
    for j in range(0, x+1):
        if j== len(r):
            break
        res += max(int(l[j]), int(r[j])) - min(int(l[j]), int(r[j]))
    print(res)