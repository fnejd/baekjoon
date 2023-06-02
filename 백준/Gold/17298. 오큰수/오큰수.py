import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

ans = [-1] * N

# 스택
stack = []

for i in range(N):
    # 스택의 top 에 해당하는 수보다 큰 수인 경우 오큰수
    while stack and A[stack[-1]] < A[i]:
        # 오큰수 저장
        ans[stack.pop()] = A[i]
    
    stack.append(i)
# 스택에 인덱스가 남아 있는 경우는 해당 하는 수의 오큰수 X

print(*ans)