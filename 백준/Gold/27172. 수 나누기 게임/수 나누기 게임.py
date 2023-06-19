import sys
input = sys.stdin.readline

N = int(input())

players = list(map(int, input().split()))
num = [False for _ in range(1000001)]

for x in players:
    num[x] = True

res = [0 for _ in range(1000001)]

for i in range(N):
    # 해당 수의 배수가 존재할 경우
    for j in range(players[i] * 2, 1000001, players[i]):
        if num[j]:
            res[players[i]] += 1
            res[j] -= 1


for i in range(N):
    print(res[players[i]], end=' ')
