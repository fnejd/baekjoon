import sys
input = sys.stdin.readline

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]
# 시작 점 기준 정렬
lines.sort(key= lambda x : (x[0], x[1]))

# 겹치치 않는 선분들만 저장
stack = []

for i in range(N):
    # 선분이 겹칠 경우 -> 겹치는 것 갱신
    if stack and stack[-1][1] >= lines[i][0]:
        x, y = stack.pop()
        # 겹치는데 끝나는 지점이 늘어날 경우
        if y < lines[i][1]:
            y = lines[i][1]
        stack.append([x, y])
    else:
    # 겹치지 않을 경우
        stack.append(lines[i])

length = 0

for x in stack:
    length += x[1] - x[0]

print(length)