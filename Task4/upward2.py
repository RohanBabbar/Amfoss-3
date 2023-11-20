t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    cnt = 0
    for j in range(n-2, -1, -1):
        while (arr[j] >= arr[j+1]):
            arr[j] = arr[j]//2
            cnt +=1
            if arr[j] == 0:
                break
    flag =1
    for j in range(n-1):
        if arr[j] >= arr[j+1]:
            flag = 0
            break
        else:
            flag = 1
    if flag:
        print(cnt)
    else:
        print(-1)