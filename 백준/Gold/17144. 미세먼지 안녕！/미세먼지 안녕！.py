import sys
input = sys.stdin.readline

# 행, 열, 초
R, C , T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

# 위쪽 공기청정기 방향
tdir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
# 아래쪽 공기청정기 방향
bdir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 남아 있는 미세먼지 양
ans = 0

#공기 청정기 가동
def airclean(start , dir):
    # 방향 갱신
    t = 0
    # 이동할 미세먼지 저장
    tmp = 0

    # 시작 위치 
    x, y = start, 1

    while True:
        nx = x + dir[t][0]
        ny = y + dir[t][1]

        #공기 청정기 도착
        if x == start and y == 0: 
            break
        # 범위 벗어났을 경우
        if nx >= R or ny >=  C or nx < 0 or ny < 0:
            # 방향 변경
            t+= 1
            continue

        # tmp 에 arr[x][y] 저장
        arr[x][y], tmp = tmp , arr[x][y]
        x , y = nx ,ny
    

def move():
    spread = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                # 인접한 4방향
                cnt = 0
                for k in range(4):
                    xx = i + tdir[k][0]
                    yy = j + tdir[k][1]

                    if 0<= xx < R and 0 <=yy < C and arr[xx][yy] != -1:
                        spread[xx][yy] += arr[i][j] // 5
                        cnt += 1
                arr[i][j] -= cnt * (arr[i][j] // 5)

    for i in range(R):
        for j in range(C):
            arr[i][j] += spread[i][j]


# 공기 청정기 위치 찾기  
for i in range(R):
      if arr[i][0] == -1:
          top = i
          bottom = i+ 1
          break
      
# 매초마다 
for _ in range(T):
    # 미세 먼지 확산
    move()
    # 공기 청정기 작동
    # 반시계 방향
    airclean(top, tdir)
    # 시계 방향
    airclean(bottom, bdir)


for i in range(R):
    for j in range(C):
        if arr[i][j] > 0 :
            ans += arr[i][j]

print(ans)   