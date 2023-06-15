import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

# 두 덩어리 이상으로 분리되는 최초의 시간

# 주위 0의 개수 구하기
# 빙산 녹이기
# 덩어리 개수 구하기 > 1 의 시간 


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

year = 1


def check(i, j, v):

    q = deque()

    q.append((i, j))

    v[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            if 0<= xx < N and 0 <= yy < M and ice[xx][yy] > 0 and not visited[xx][yy]:
                q.append((xx, yy))
                v[xx][yy] = True

while True:

    # 주위 0의 개수 담기
    melted = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 빙산 없는 경우 건너뛰기
            if ice[i][j] == 0:
                continue

            for k in range(4):
                if ice[i + dx[k]][j + dy[k]] == 0:
                    melted[i][j] += 1
    
    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0:
                # 다 녹아도 0 이상
                ice[i][j] = max(0, ice[i][j] - melted[i][j])
    
    # 덩어리 구하기
    # 2 덩어리로 나뉘면 년도 반환
    # 덩어리 0 -> 0 출력
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ice[i][j] > 0:
                check(i, j, visited)
                cnt += 1
                if cnt > 1 :
                    print(year)
                    exit(0)
    
    if cnt == 0:
        # 덩어리가 하나도 없을 경우
        print(0)
        break
    year += 1
