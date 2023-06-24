import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = sys.maxsize
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a, b ,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


tmp = INF
# 가장 작은 사이클 찾기
for i in range(1, V+1):
    if graph[i][i] < tmp:
        tmp = graph[i][i]

if tmp != INF:
    print(tmp)
else:
    print(-1)