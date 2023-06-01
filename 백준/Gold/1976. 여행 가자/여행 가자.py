import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

p = [i for i in range(N+1)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])    
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


for i in range(N):
    graph = list(map(int, input().split()))

    for j in range(N):
        if graph[j] == 1:
            union(i+1, j+1)


arr = list(map(int, input().split()))

ans = []

# 루트 담기
for x in arr:
    ans.append(find_set(x))


if(len(set(ans))) == 1:
    print("YES")
else:
    print("NO")