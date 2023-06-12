import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

village = list(map(int, input().strip().split()))
village.insert(0,0)

# 마을 연결 정보
link = dict()

for _ in range(N-1):
    a, b = map(int, input().strip().split())

    if a not in link:
        link[a] = [b]
    else:
        link[a].append(b)
    
    if b not in link:
        link[b] = [a]
    else:
        link[b].append(a)


# 1. 우수 마을 주민 수 총합 최대
# 2. 우수 마을끼리는 인접 불가능
# 3. 선정되지 못한 마을은 적어도 하나 이상의 우수 마을과 인접 (우수마을을 선정하는 것이 이득)

# 인근에 우수 마을 없을 때 선택!

visit = [False for _ in range(N+1)]
# dp[n][0] : 해당 마을이 우수 마을  X 주민수  총합 -  (dp[자식노드][0], dp[자식노드][1] ) 자식노드의 최대값
# dp[n][1] : 해당 마을이 우수 마을 O 주민수  총합 - 자식 마을은 우수 마을 X (dp[자식마을][0]) + n마을 사람들 수(우수마을)
dp = [[0, 0] for _ in range(N+1)]


# 어떤 노드를 ROOT 로 선택해도 OK (사이클 없으므로)
# TOP - DOWN 다시 leaf 에서 올라오면서 갱신

def dfs(n):
    visit[n] = True
    # 해당 마을의 주민수
    dp[n][1] += village[n]

    for x in link[n]:
        if not visit[x]:
            dfs(x)
            # 해당 마을이 우수 마을  X -> (dp[자식노드][0], dp[자식노드][1] ) 자식노드의 최대값
            dp[n][0] += max(dp[x][0], dp[x][1])
            # 해당 마을이 우수 마을 O -> 자식 마을은 우수 마을 X 
            dp[n][1] += dp[x][0]

# 루트노드 선택
dfs(1)
# 루트노드에서의 최대값
print(max(dp[1]))

