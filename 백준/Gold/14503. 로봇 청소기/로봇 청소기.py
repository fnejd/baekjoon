

# 왼쪽 방향 회전
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 로봇 좌표, 방향
# 0 : N, 1 : E, 2 : S, 3 : W
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

def robot(x, y, d):
    # 청소 칸 수
    global cnt

    while True:
        # 청소하기
        if room[x][y] == 0:
            room[x][y] = 2  
            cnt += 1    

        for _ in range(4):
            # 왼쪽 방향 회전
            d = (d + 3) % 4
            xx = x + dx[d]
            yy = y + dy[d]
            # 왼쪽 방향으로 회전했을 때 청소가 안 되었다면 
            if 0<= xx < N and 0 <= yy < M and room[xx][yy] == 0:
                # 청소 안 한 곳으로 이동 ->  청소하기 단계
                x = xx
                y = yy
                break
        # 4방향 모두 청소가 된 경우
        else:
            # 후진했을 때 벽
            if room[x - dx[d]][y - dy[d]] == 1:
                print(cnt)
                break
            # 후진 가능         
            else:
                # 후진
                x -= dx[d]
                y -= dy[d]

robot(r, c, d)