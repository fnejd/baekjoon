import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

ans = sys.maxsize

left = 0
right = 0
tmp = 0

while True:

    if tmp >= S:
        # 최소 개수 갱신
        ans = min(ans, right-left)
        tmp -= arr[left]
        # 시작 위치 이동
        left += 1
    else:
        if right == N:
            break
        tmp += arr[right]
        right += 1

if ans < sys.maxsize:
    print(ans)
else:
    print(0)