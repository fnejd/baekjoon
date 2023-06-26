import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a][b] = 1

# 키 대소 관계 연결
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

num = 0

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        # 현재 학생보다 키가 작은 학생과 큰 학생 수 모두 세기
        cnt += graph[i][j] + graph[j][i]
    if cnt == N-1:
        num += 1

print(num)
