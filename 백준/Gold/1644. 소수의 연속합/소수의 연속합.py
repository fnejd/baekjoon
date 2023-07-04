import sys
input = sys.stdin.readline

N = int(input())

# 소수찾기
arr = [False for _ in range(N+1)]
num = []

# 에라토스테네스의 체
for i in range(2,N+1):
    if arr[i] == False:
        num.append(i)
        for j in range(2 * i, N+1, i):
            arr[j] = True

cnt = 0
i = 0
j = 0

while j <= len(num):
    # 연속 소수 합
    tmp = sum(num[i:j])

    if tmp == N:
        cnt += 1
        j += 1
    elif tmp > N:
        i += 1
    else:
        j += 1

print(cnt)