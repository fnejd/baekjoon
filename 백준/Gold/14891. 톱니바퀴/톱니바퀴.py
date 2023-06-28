from collections import deque

wheel = [input() for _ in range(4)]

N = int(input())

for _ in range(N):
    idx, dir = map(int, input().split())

    # 현재 회전 시키는 톱니바퀴 왼쪽 중간, 오른쪽 중간 확인
    d = [0] * 4
    d[idx-1] = dir

    v = [False] * 4
    v[idx-1] = True

    q = deque()
    # 1~4 방향 확인
    q.append(idx-1)

    while q:
        tmp = q.popleft()

        rx = tmp + 1
        lx = tmp - 1
        if 0 <= rx <= 3 and not v[rx]:
            if d[tmp] != 0 and wheel[tmp][2] != wheel[rx][-2]:              
                d[rx] = d[tmp] * -1
            v[rx] = True
            q.append(rx)
        
        if 0<= lx <= 3 and not v[lx]:
            if d[tmp] != 0 and wheel[tmp][-2] != wheel[lx][2]:
                d[lx] = d[tmp] * -1
            v[lx] = True
            q.append(lx)
            
    # 돌리기
    for i in range(4):
        # 시계 방향
        if d[i] == 1:
            wheel[i] = wheel[i][-1] + wheel[i][:-1]
        # 반시계 방향
        elif d[i] == -1:
            wheel[i] = wheel[i][1:] + wheel[i][0]
    
ans = 0
for i in range(4):
    if wheel[i][0] == '1':
        ans += 2 ** (i)

print(ans)