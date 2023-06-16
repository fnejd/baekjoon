import sys
input = sys.stdin.readline
from collections import deque

t = int(input())


def bfs(hx, hy):
    q = deque()
    # 시작점
    q.append((hx, hy))

    while q:
        x, y = q.popleft()
        # 현재 위치에서 페스티벌까지 1000 이하면 도달 가능
        if abs(x - fx) + abs(y - fy) <= 1000:
            print("happy")
            return
        
        for i in range(N):
            if not visit[i]:
                # 1000 이하면 다음 편의점 이동 가능
                if abs(x - store[i][0]) + abs(y - store[i][1]) <= 1000:
                    visit[i] = True
                    q.append(store[i])
    
    print("sad")
    return 

for T in range(t):
    N = int(input())

    hx, hy = map(int, input().split())

    store = [list(map(int, input().split())) for _ in range(N)]

    fx , fy = map(int, input().split())

    # 편의점 방문 여부
    visit = [False for _ in range(N)]

    bfs(hx, hy)
