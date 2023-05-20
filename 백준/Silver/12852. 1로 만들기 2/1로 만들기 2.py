import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
res = [0] * (N+1)

# 1만들기 
for i in range(2, N+1):

    #1로 뺐을 때와 3으로 나누었을 때와, 2로 나누었을 때 비교해서 최소의 경우 갱신

    # 1을 뺐을 경우
    dp[i] = dp[i-1] + 1
    res[i] = i-1

    # 3으로 나누었을 경우
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        res[i] = i // 3
    
    # 2로 나누었을 경우
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        res[i] = i // 2

# 연산 최소값 
print(dp[N])

# 1로 만드는 방법 출력
start = N
while start != 0:
    print(start, end = ' ')
    start = res[start]