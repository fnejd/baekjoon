import sys
input = sys.stdin.readline

N = int(input())

point = [list(map(int, input().split())) for _ in range(N)]

# 사선 공식 이용
point.append(point[0])

x, y = 0, 0

for i in range(N):
    x += point[i][0] * point[i+1][1]
    y += point[i][1] * point[i+1][0]

# 반올림 
print(round(abs((x-y)/2),1))