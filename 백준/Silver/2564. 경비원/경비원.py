import sys
input = sys.stdin.readline

BX, BY = map(int, input().split())

N = int(input())

dis = []

# 방향
# 1 : 북, 2 : 남, 3 : 서, 4: 동

# 왼쪽 위 꼭지점으로부터의 거리
def distance(d, p):
    if d == 1:
        return p
    elif d == 2:
        return BX + BY + (BX - p)
    elif d == 3:
        return 2 * BX + BY + (BY - p)
    else:
        return BX + p


for _ in range(N):
    d, p = map(int, input().split())

    dis.append(distance(d, p))


# 동근 위치
x, y = map(int, input().split())
# 왼쪽 위 꼭지점으로부터 동근의 거리
l = distance(x, y)

# 각 상점 사이 최단 거리의 합
res = 0

for i in range(N):
    # 동근이의 거리와 상점의 거리 차이, 전체 거리에서 - (동근이의 거리, 상점의 거리 차이) 중 최소값 저장
    res += min(abs(l-dis[i]), 2 * BX + 2 * BY - abs(l-dis[i]))

print(res)