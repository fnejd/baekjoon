import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

ticket = []

for i in range(N):
    ticket += list(input().split())

# 정렬된 입장 순서
sort_ticket =  sorted(ticket, key=lambda x : (x.split("-")[0], int(x.split("-")[1])))

stack = deque()

j = 0
i = 0
while i < 5 * N and j < 5 * N:
    # 정렬된 입장 순서와 비교
    # 일치하면 입장
    if ticket[i] == sort_ticket[j]:
        j += 1
        i += 1
    else:
        # 불일치할 경우 스택의 최상단과 일치하면 stack pop
        if stack and stack[-1] == sort_ticket[j]:
            stack.pop()
            j += 1
        else:
            # 스택의 최상단과 불일치하면 stack 에 push
            stack.append(ticket[i])
            i += 1

while stack:
    if stack[-1] == sort_ticket[j]:
        stack.pop()
        j += 1
    else:
        break

# stack에 남아 있으면 BAD
if stack:
    print("BAD")
else:
    print("GOOD")