import sys
input = sys.stdin.readline

T = int(input())

fibo = [1 for _ in range(68)]

fibo[2] = 2
fibo[3] = 4

for i in range(4, len(fibo)):
    fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3] + fibo[i-4]

for t in range(T):
    n = int(input())
    print(fibo[n])