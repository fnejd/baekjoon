import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

left = 0
right = N-1

res = sys.maxsize
#0에 가장 가까운 값
ans = 0

while left < right:
    tmp = arr[left] + arr[right]

    if abs(tmp) < res:
        ans = tmp
        res = abs(tmp)
    
    if tmp < 0:
        left += 1
    elif tmp > 0 :
         right -= 1
    else:
        break

print(ans)