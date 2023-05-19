N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

# (i , j)까지의 합 저장
for i in range(1,N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]
    

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())

    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])