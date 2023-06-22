import sys
input = sys.stdin.readline

N = int(input())

arr = sorted(list(map(int, input().split())))

left = 0
right = N-1

ans_l = 0
ans_r = 0
ans = sys.maxsize

while left < right:
    tmp = arr[left] + arr[right]

    if abs(tmp) < ans:
        ans = abs(tmp)
        ans_l = arr[left]
        ans_r = arr[right]
    
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        break


print(ans_l, ans_r)