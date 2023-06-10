import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

cnt = dict()

# 수열에서 등장 횟수
for x in A:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 0

res = [-1] * N

stack = []

for i in range(N):
    # 오등큰수인 경우
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)

print(*res)