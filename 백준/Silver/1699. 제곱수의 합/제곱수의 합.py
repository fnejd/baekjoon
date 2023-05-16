N = int(input())

dp = [i for i in range(N+1)]

# 최소항의 개수
for i in range(1, N+1):
    for j in range(1, i+1):
        if i < j * j:
            break
        # j*j 인 경우 추가
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[N])