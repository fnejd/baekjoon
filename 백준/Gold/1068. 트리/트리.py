import sys
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
num = int(input())

def tree(node):
    # 현재 노드 삭제 처리 
    parent[node] = -10
    for i in range(N):
        # 현재 삭제하는 노드의 자식 노드들 삭제
        if parent[i] == node:
            tree(i)

tree(num)

# 리프 노드 -> 루트 노드 X, 자식 노드가 없을 때 (다른 노드의 부모가 X)
cnt = 0

for i in range(N):
    # 삭제 되지 않은 노드
    if parent[i] != -10:
        # 해당 노드의 자식이 없을 경우
        if i not in parent:
            cnt += 1

print(cnt)
