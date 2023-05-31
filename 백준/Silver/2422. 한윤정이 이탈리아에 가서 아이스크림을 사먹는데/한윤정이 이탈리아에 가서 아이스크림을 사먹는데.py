import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 가능한 조합 여부
check =[[True for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x , y = map(int, input().split())

    check[x][y] = False
    check[y][x] = False

cnt = 0

# 3가지 조합
for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if check[i][j] and check[j][k] and check[i][k]:
                cnt += 1

print(cnt)
