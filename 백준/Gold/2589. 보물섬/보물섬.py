import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]

# 보물 최단 거리 이동 시간
ans = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def treasure(i, j):
    q = deque()
    q.append((i, j, 0))
    visit[i][j] = True
    #해당 위치 기준으로 가장 먼곳까지의 최단 거리 이동시간 구하기
    tmp = 0

    while q:
        x, y, cnt = q.popleft()
        tmp = cnt

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            if 0<= xx < R and 0<= yy < C and visit[xx][yy] == False and arr[xx][yy] == 'L':
                q.append((xx, yy, cnt + 1))
                visit[xx][yy] = True
                
    return tmp


for i in range(R):
    for j in range(C):
        # 섬일 경우 보물 찾기 시작
        if arr[i][j] == 'L':
            visit = [[False for _ in range(C)] for _ in range(R)]
            # 서로 간에 가장 긴 시간이 걸리는 육지에 있기 때문에 최대값 갱신
            ans = max(ans, treasure(i, j))


print(ans)