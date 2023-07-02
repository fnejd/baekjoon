import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

T = int(input())

for t in range(T):
    n, d, c = map(int, input().rstrip().split())

    graph = [[] for _ in range(n+1)]
    # 거리
    dis = [INF for _ in range(n+1)]

    for D in range(d):
        a, b, s = map(int, input().rstrip().split())
        graph[b].append((a, s))
    
    # 시작점
    dis[c] = 0
    queue = []
    heapq.heappush(queue, (0, c))

    while queue:
        #시간, 컴퓨터 번호
        time, num = heapq.heappop(queue)

        for next, cost in graph[num]:
            tmp = time + cost

            if tmp < dis[next]:
                dis[next] = tmp
                heapq.heappush(queue, (tmp, next))

    # 감염되는 컴퓨터
    computer = 0
    # 시간
    ans = 0

    for x in dis:
        if x != INF:
            computer +=1 
            ans = max(x, ans)
    
    print(computer, ans)