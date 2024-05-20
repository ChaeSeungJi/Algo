n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
ans = 0
idx = 1
while k > 0:
    ans += (k // arr[-idx])
    k %= arr[-idx]
    idx += 1
print(ans)
