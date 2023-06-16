import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 집 -> 치킨거리 구하기

# M 개 치킨 남기는 모든 조합
import sys
input = sys.stdin.readline

house = []
chicken = []

# 집들의 위치
# 치킨집들의 위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

res = sys.maxsize

# 선택한 치킨집들
arr = []

def dis(arr):
    # 집, 치킨집 거리
    sum = 0

    for i in range(len(house)):
        # 집마다 선택한 치킨 집 조합 중에서 가까운 치킨집 거리 구하기
        tmp = 2 * N
        for j in range(len(arr)):
            tmp = min(tmp, abs(house[i][0] - arr[j][0]) + abs(house[i][1] - arr[j][1]))
        # 가장 가까운 치킨 집과의 거리     
        sum += tmp

    return sum


def dfs(cnt, arr):
    global res

    if len(arr) > M:
        return 
    
    if cnt == len(chicken):
        if len(arr) == M:
            # 최소값 갱신
            res = min(res, dis(arr))
        return
    
    # 선택하는 경우
    dfs(cnt + 1, arr + [chicken[cnt]])
    # 선택 안하는 경우
    dfs(cnt + 1, arr)


dfs(0, arr)

print(res)