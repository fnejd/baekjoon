import sys
input = sys.stdin.readline
import heapq

INF = sys.maxsize

N, E = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().rstrip().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())



# 출발점 -> v1 -> v2 -> N
# 출발점 -> v2 -> v1 -> N

def dijkstra(s, e):
    dis = [INF for _ in range(N+1)]
    dis[s] = 0
    queue = []

    heapq.heappush(queue, (0, s))

    while queue:
        d, node = heapq.heappop(queue)

        # 최소값을 구하려는 것
        if dis[node] < d:
            continue

        for next, cost in graph[node]:
            tmp = dis[node] + cost

            if tmp < dis[next]:
                dis[next] = tmp
                heapq.heappush(queue, (tmp, next))
    
    return dis[e]

# 두가지 경로 존재
res_v1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
res_v2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if res_v1 >= INF and res_v2 >= INF:
    print(-1)
else:
    print(min(res_v1, res_v2))
