t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print('YES' if n % m == 0 else 'NO')