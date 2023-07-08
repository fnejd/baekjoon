import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

# 
arr = []

ans = 0

def dfs(x):
    global ans
    
    if x == N:
        sum = 0
        for i in range(N-1):
            sum += abs(A[arr[i+1]] - A[arr[i]])
        ans = max(ans, sum)
        return
    
    for i in range(N):
        if i not in arr:
            arr.append(i)
            dfs(x+1)
            arr.pop()

        
dfs(0)
print(ans)