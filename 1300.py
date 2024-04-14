# https://www.geeksforgeeks.org/binary-search/?ref=outind

import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
start = 1
end = K

while start <= end:
    mid = (start + end) // 2    # 중간값 찾기
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)   # 그 행의
    if cnt >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        # 막 이렇게 start와 end범위 옮겨가면서 탐색 범위 줄임
print(result)
