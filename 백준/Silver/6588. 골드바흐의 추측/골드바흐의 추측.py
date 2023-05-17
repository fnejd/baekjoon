import sys
input = sys.stdin.readline


check = [True] * 1000001

# 소수 여부 배열
for i in range(2, 1000001):
    if check[i]:
        # 해당 수의 배수는 소수 아님
        for j in range(i*2, 1000001, i):
            check[j] = False

while True:
    n = int(input())

    if n == 0:
        break
    #두 홀수 소수 찾기
    for i in range(3, n+1, 2):
        if check[i] and check[n-i]:
            # 두 홀수 소수 중에서 차이가 가장 큰 것 출력
            print(n,'=',i,'+',n-i)
            flag = True
            break
    else:
        print("Goldbach's conjecture is wrong.")