from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1 ,0, 1, 1, 1]

def bfs(i, j):

    q = deque()
    q.append((i, j))
    visit[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(8):
            xx = x + dx[k]
            yy = y + dy[k]
            # 땅이고 방문 안한 경우
            if 0<= xx < h and 0<= yy <w and visit[xx][yy] == False:
                if arr[xx][yy] == 1:
                    visit[xx][yy] = True
                    q.append((xx, yy))


while True:
    w, h = map(int, input().split(" "))

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split(" "))) for _ in range(h)]
    # 방문 체크
    visit = [[False for _ in range(w)] for _ in range(h)]
    # 섬의 개수
    cnt = 0

    for i in range(h):
        for j in range(w):
            # 방문 안하고 땅인 경우 같은 섬 방문 체크
            if visit[i][j] == False and arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)
