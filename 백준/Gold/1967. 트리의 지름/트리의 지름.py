import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 노드 개수
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, w = map(int, input().split())

    graph[x].append([y, w])
    graph[y].append([x, w])


def dfs(n, w):
    for x ,y in graph[n]:
        if weight[x] == -1:
            # 방문하지 않은 노드
            weight[x] = w + y # 현재 노드까지 가중치 저장
            dfs(x, weight[x])


weight = [-1 for _ in range(N+1)]

# 루트 노드는 1
weight[1] = 0
dfs(1, 0)

# 루트 노드 기준으로 최대 가중치가 저장되어 있는 노드 선택
end = weight.index(max(weight))

weight = [-1 for _ in range(N+1)]
# 선택한 노드를 루트 노드라고 설정하고 해당 노드 기준으로 최대 가중치 저장되어 있는 노드 선택
weight[end] = 0
dfs(end, 0)

print(max(weight))
