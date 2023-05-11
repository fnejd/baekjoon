import heapq
import sys
input = sys.stdin.readline

# 보석 개수, 가방 개수
N, K = map(int, input().split(" "))

jewel = []
b_weight = []

for _ in range(N):
    # 보석 무게, 가격
    M, V = map(int, input().split(" "))
    heapq.heappush(jewel, (M, V))

for _ in range(K):
    #가방에 담을 수 있는 최대 무게
    b_weight.append(int(input()))

#가방은 오름차순 정렬
b_weight.sort()

# 훔칠 수 있는 보석 가격의 최대값
ans = 0

# 보석 가격 저장
price = []

for b in b_weight:
    # 현재 가방 무게가 보석 무게보다 클 경우 해당 보석 가격 높은 순으로 힙에 저장
    while jewel:
        if b >= jewel[0][0]:
            W, P = heapq.heappop(jewel)
            #최대힙으로 저장
            heapq.heappush(price, -P)
        else:
            break
    # 보석 가격 담은 힙이 비어 있지 않은 경우 가격 저장
    if price:
        ans -= heapq.heappop(price)
    
print(ans)