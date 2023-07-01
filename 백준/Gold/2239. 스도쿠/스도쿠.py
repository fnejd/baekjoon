import sys
input = sys.stdin.readline
arr = [list(map(int, input().rstrip())) for _ in range(9)]

# 0 일 경우
# 가로 , 세로, 3 * 3 에서 없는 숫자 넣기


def row(c, n):
    for i in range(9):
        if arr[i][c] == n:
            return False
    return True

def col(r, n):
    for i in range(9):
        if arr[r][i] == n:
            return False
    return True

def square(r, c, n):
    sr = (r // 3) * 3
    sc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            if arr[sr + i][sc + j] == n:
                return False
    return True

def sudoku(x):
    # 채워야 하는 위치 다 채웠을 경우
    if x == len(pos):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end = '')
            print()
        #출력 초과 해결
        exit()
    
    r, c = pos[x]

    for n in range(1, 10):
        # 가로, 세로, 3 * 3 넣어도 되는지 확인
        if row(c, n) and col(r, n) and square(r, c, n):
            arr[r][c] = n
            sudoku(x + 1)
            arr[r][c] = 0

# 채워야 하는 위치 저장
pos = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos.append([i, j])


sudoku(0)