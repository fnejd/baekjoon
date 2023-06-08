import sys
input = sys.stdin.readline

N = int(input())

mem = list(map(int, input().split()))

# 왼쪽에 있는 사람 수가 0 인 경우  비어 있는 자리에 바로 넣기
ans = [0] * N

for i in range(N):
    # 왼쪽 키 큰 사람 수
    num = 0
    for j in range(N):
        # 왼쪽 키 큰 사람 수 일치, 비어 있는 자리인 경우
        if num == mem[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        # 키큰 사람 자리
        elif ans[j] == 0:
            num += 1

print(*ans)