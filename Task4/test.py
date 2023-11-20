n = int(input())
inp = []

for i in range(n):
    row = list(map(int, input().split()))
    inp.append(row)
column_sums = [sum(inp[j][i] for j in range(n)) for i in range(3)]
if all(sum == 0 for sum in column_sums):
    print("YES")
else:
    print("NO")
