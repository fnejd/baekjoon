import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 방문체크
check = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 섬에 번호 지정
mark = 1

# 섬을 구분, 같은 섬에 포함되면 같은 번호
def land(i, j):

    queue = deque()
    queue.append((i, j))
    check[i][j] = True
    arr[i][j] = mark

    while queue:
        lx, ly = queue.popleft()

        for k in range(4):
            xx = lx + dx[k]
            yy = ly + dy[k]

            if 0<= xx < N and 0<= yy < N and check[xx][yy] == False and arr[xx][yy] == 1:
                queue.append((xx, yy))
                check[xx][yy] = True
                arr[xx][yy] = mark
   

#섬에 번호 지정
for i in range(N):
    for j in range(N):
        # 섬이면서 방문하지 않은 경우
        if arr[i][j] == 1 and check[i][j] == False:
            land(i, j)
            mark += 1


# 다리 길이 구하기
def bridge(x, y, num):

    visit[x][y] = True

    q = deque()
    q.append((x, y, 0))

    while q:

        nx, ny, cnt= q.popleft()

        # 다른 섬 도착, 다른 섬에 도달하기까지 거리 반환
        if arr[nx][ny] != 0 and arr[nx][ny] != num:
            return cnt
        
        # 4방 탐색
        for k in range(4):
            xx = nx + dx[k]
            yy = ny + dy[k]
            # 범위를 벗어나면 안되고 현재 섬과 같은 섬이면 안된다. 
            if 0<= xx < N and 0 <= yy < N and visit[xx][yy] == False and arr[xx][yy] != num:
                
                q.append((xx , yy, cnt + 1))
                visit[xx][yy] = True

    return ans


# 거리 최대로 초기화
ans = sys.maxsize


for i in range(N):
    for j in range(N):
        # 섬인 경우
        if arr[i][j] != 0:
            visit = [[False for _ in range(N)] for _ in range(N)]
            #최단 거리 갱신
            ans = min(ans, bridge(i, j, arr[i][j]))

# 다른 섬에 도달하기 까지의 거리가 포함되었으므로 다리 길이 구하기 위해 1 빼기                    
print(ans-1)