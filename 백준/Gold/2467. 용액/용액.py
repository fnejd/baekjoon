import sys
input = sys.stdin.readline

N = int(input())

# 오름차순으로 정렬 되어 있는 상태
arr = list(map(int, input().split()))


left = 0
right = N-1

res_l = 0
res_r = 0
value = sys.maxsize

while left < right:
    tmp = arr[left] + arr[right]
    # 절댓값 중 가장 작은 값 저장
    if abs(tmp) < value:
        value = abs(tmp)
        res_l = arr[left]
        res_r = arr[right]
    
    if tmp > 0: 
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        # 0일 경우
        break

    
# 오름차순 출력
print(res_l, res_r)