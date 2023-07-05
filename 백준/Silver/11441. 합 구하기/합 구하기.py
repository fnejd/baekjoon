import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

A_sum = [0] * (N+1)

# 누적합
for i in range(N):
    A_sum[i] = A_sum[i-1] + A[i]

M = int(input())

for _ in range(M):
    i, j = map(int, input().split())

    print(A_sum[j-1] - A_sum[i-2])