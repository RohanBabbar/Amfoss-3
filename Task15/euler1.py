n = int(input())
for x in range(n):
    a = int(input())
    l = []

    for i in range(a):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)

    total_sum = sum(l)
    print(total_sum)
