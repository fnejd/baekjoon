import sys
input = sys.stdin.readline

N, K = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    graph[x][y] = 1

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if graph[s][k] and graph[k][e] :
                # 전후 관계 연결하기
                graph[s][e] = 1


S = int(input())

for _ in range(S):
    x, y = map(int, input().split())

    if graph[x][y] == 1:
        print(-1)
    elif graph[y][x] == 1:
        print(1)
    else:
        print(0)