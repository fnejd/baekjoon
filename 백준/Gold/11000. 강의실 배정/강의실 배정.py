import sys
input = sys.stdin.readline
import heapq

# 우선순위큐 사용
# 끝나는 시간이 빠른 강의 순서

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

# 시작 시간 기준으로 정렬
arr.sort()

queue = []

for i in range(N):
    # 다음 강의가 현재 큐에 있는 끝나는 시간이 빠른 시간 강의 이후에 시작
    # 강의 시간 겹치지 X -> 현재 큐에 있는 끝나는 시간이 빠른 강의 꺼내기
    if queue and queue[0] <= arr[i][0] :
        heapq.heappop(queue)

    heapq.heappush(queue, arr[i][1])

# 큐에 필요한 강의실 개수 만큼이 남는다
print(len(queue))

