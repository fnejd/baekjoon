import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))

# 경우의 수
cnt = 0

left = 0
right = 1

while left < N and right <= N:

    res = sum(A[left:right])

    if res == M:
        cnt += 1
        right += 1

    elif res < M:
        right += 1
    
    else:
        left += 1

print(cnt)
