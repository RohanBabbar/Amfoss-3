n=int(input())
for i in range (n):
    x=int(input())
    set=[]
    for j in range(x):
        set.append(input().split())
    res=[]
    for j in range(x-1):
        arr1=[0,set[0][0]]
        arr2=[0,'']
        for k in range(x):
            if set[k][0] not in arr1:
                arr2[1]=set[k][0]
                arr2[0]+=1
            else:
                arr1[0]+=1
        if arr2[0]>arr1[0]:
            arr1[1]=arr2[1]
        res.append(arr1[1])

        for k in range(x):
            if len(set[k])==0:
                continue
            if set[k][0]==arr1[1]:
                set[k].pop(0)
    if len(set[0])==0:
        res.append(set[1][0])
    else:
        res.append(set[0][0])
    for j in res:
        print(j+" ",end="")
    print()