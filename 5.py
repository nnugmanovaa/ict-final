n = int(input())
for k in range(n):
    a = n
    for j in range(k):
        a = a - (k-j)*(j+1)
    if a < 0:
        break
    else:
        ans = k
print(ans)