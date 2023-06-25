import sys
input = sys.stdin.readline

N = int(input())

max_arr = [0, 0, 0]
min_arr = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().rstrip().split())

    max_arr = [max(max_arr[0], max_arr[1]) + a, 
               max(max_arr[0], max_arr[1], max_arr[2]) + b, 
               max(max_arr[1], max_arr[2]) + c]
    min_arr = [min(min_arr[0], min_arr[1]) + a,
                min(min_arr[0], min_arr[1], min_arr[2]) + b,
                min(min_arr[1], min_arr[2]) + c]

print(max(max_arr), min(min_arr))